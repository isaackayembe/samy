from django import forms

class MonFormulaire(forms.Form):
    nom = forms.CharField(max_length=100, label='Nom')
    postnom = forms.CharField(max_length=100, label='Postnom')
    prenom = forms.CharField(max_length=100, label='Prénom')
    GENRE_CHOICES = [
        ('couple', 'Couple'),
        ('singleton', 'Singleton'),
    ]
    genre = forms.ChoiceField(choices=GENRE_CHOICES, label='Genre')