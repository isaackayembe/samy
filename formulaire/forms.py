from django import forms

class MonFormulaire(forms.Form):
    nom = forms.CharField(
        max_length=100,
        label='Nom',
        widget=forms.TextInput(attrs={'class': 'form-control'})  # Ajout de la classe Bootstrap
    )
    postnom = forms.CharField(
        max_length=100,
        label='Postnom',
        widget=forms.TextInput(attrs={'class': 'form-control'})  # Ajout de la classe Bootstrap
    )
    prenom = forms.CharField(
        max_length=100,
        label='Prénom',
        widget=forms.TextInput(attrs={'class': 'form-control'})  # Ajout de la classe Bootstrap
    )
    GENRE_CHOICES = [
        ('couple', 'Couple'),
        ('singleton', 'Singleton'),
    ]
    genre = forms.ChoiceField(
        choices=GENRE_CHOICES,
        label='Genre',
        widget=forms.Select(attrs={'class': 'form-select'})  # Ajout de la classe Bootstrap
    )