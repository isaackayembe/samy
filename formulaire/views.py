from django.shortcuts import render, redirect, get_object_or_404
from .forms import MonFormulaire
from .models import Participant
from django.shortcuts import render, redirect
from .forms import MonFormulaire
from .models import Participant
from django.http import HttpResponse
from .models import Participant
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from django.shortcuts import render
from .models import Participant
from django.http import HttpResponse
import pandas as pd
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import requests 
from django.contrib import messages
from collections import Counter  # Assurez-vous d'importer Counter

def generer_lien(request):
    return render(request, 'lien.html')


def remplir_formulaire(request):
    message = None
    if request.method == 'POST':
        form = MonFormulaire(request.POST)
        if form.is_valid():
            # Vérification de l'existence du participant
            participant_existant = Participant.objects.filter(
                nom=form.cleaned_data['nom'],
                postnom=form.cleaned_data['postnom'],
                prenom=form.cleaned_data['prenom'],
                genre=form.cleaned_data['genre']
            ).exists()

            if participant_existant:
                message = "Votre présence a déjà été enregistrée, cher invité."
                return render(request, 'formulaire.html', {'form': form, 'message': message})

            # Créer une instance de Participant et l'enregistrer
            participant = Participant(
                nom=form.cleaned_data['nom'],
                postnom=form.cleaned_data['postnom'],
                prenom=form.cleaned_data['prenom'],
                genre=form.cleaned_data['genre']
            )
            participant.save()  # Enregistrer dans la base de données

            # Rediriger vers la page de succès
            return redirect('success')  # Assurez-vous que 'success' est le nom de votre route

    else:
        form = MonFormulaire()  # Créer une nouvelle instance de formulaire

    return render(request, 'formulaire.html', {'form': form, 'message': message})

@login_required

def liste_liens(request):
    participants = Participant.objects.all()  # Récupère tous les participants
    count_participants = participants.count()  # Compte le nombre de participants

    # Comptez les boissons
    boissons = [participant.boisson for participant in participants]
    boissons_conjoints = [participant.boisson_conjoint for participant in participants]
    
    # Combinez les deux listes
    toutes_les_boissons = boissons + boissons_conjoints
    boisson_count = Counter(toutes_les_boissons)  # Utilisez Counter ici

    return render(request, 'liste_liens.html', {
        'participants': participants,
        'count': count_participants,
        'boisson_count': boisson_count.items(),  # Passez les items du Counter
    })

def telecharger_pdf(request):
    # Créer un buffer pour le PDF
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Récupérer tous les participants
    participants = Participant.objects.all()

    # Ajouter des données au PDF
    y = height - 40
    for participant in participants:
        p.drawString(100, y, f"{participant.id}, {participant.nom} ,{participant.nom_conjoint}, {participant.postnom}, {participant.prenom}, {participant.genre}, {participant.boisson}, {participant.boisson_conjoint}")
        y -= 20

    p.showPage()
    p.save()

    # Retourner le PDF en tant que réponse
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')

def telecharger_xlsx(request):
    # Récupérer tous les participants
    participants = Participant.objects.all().values('id','nom', 'nom_conjoint','postnom', 'prenom', 'genre', 'boisson', 'boisson_conjoint')

    # Convertir en DataFrame pandas
    df = pd.DataFrame(participants)

    # Créer une réponse HTTP avec un fichier Excel
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=participants.xlsx'
    
    # Écrire le DataFrame dans le fichier Excel
    df.to_excel(response, index=False)

    return response

def base(request):
    # Affiche la page de base
    return render(request, 'base.html')

def success(request):
    # Affiche la page de base
    return render(request, 'erreur.html')
def authetification(request):  # Correction de la faute de frappe dans le nom de la fonction
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('liste_liens')  # Redirigez vers la page d'accueil ou une autre page
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})  # Correction de l'indentation

    return render(request, 'login.html')  # Correction du nom du template 

def logout_view(request):
    logout(request)
    messages.success(request, "Vous avez été déconnecté avec succès.")
    return redirect('authetification')