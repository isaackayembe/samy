from django.contrib import admin
from .models import Participant

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'postnom', 'genre')  # Affiche ces champs dans l'admin
    search_fields = ('prenom', 'nom', 'postnom')  # Permet la recherche par ces champs