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
        ('1', 'Couple'),
        ('0', 'Singleton'),
    ]
    genre = forms.ChoiceField(
        choices=GENRE_CHOICES,
        label='Genre',
        widget=forms.Select(attrs={'class': 'form-select'})  # Ajout de la classe Bootstrap
    )
    
    BOISSON_CHOICES = [
        ('fantan', 'Fantan'),
        ('coca', 'Coca'),
        ('vitalo', 'Vitalo'),
        ('eau', 'Eau'),
        ('primus', 'Primus'),
        ('turbo', 'Turbo'),
        ('nkoyi_likofi', 'Nkoyi Likofi'),
        ('nkoyi_grand', 'Nkoyi Grand'),
        ('heineken', 'Heineken'),
        ('beaufort', 'Beaufort'),
        ('castel', 'Castel'),
        ('tembo', 'Tembo'),
    ]
    boisson = forms.ChoiceField(
        choices=BOISSON_CHOICES,
        label='Boisson',
        widget=forms.Select(attrs={'class': 'form-select'})  # Ajout de la classe Bootstrap
    )
    nom_conjoint = forms.CharField(
        max_length=100,
        label='Nom du Conjoint',
        required=False,  # Optionnel
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    nom_conjoint = forms.CharField(
        max_length=100,
        label='Nom du Conjoint',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    boisson_conjoint = forms.ChoiceField(
        choices=BOISSON_CHOICES,
        label='Boisson du Conjoint',
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )