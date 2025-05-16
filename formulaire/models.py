from django.db import models

class Participant(models.Model):
    nom = models.CharField(max_length=100)
    postnom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    genre = models.CharField(max_length=10, choices=[
        ('couple', 'Couple'),
        ('singleton', 'Singleton'),
    ])
    boisson = models.CharField(max_length=50, choices=[
        ('fanta', 'Fanta'),
        ('coca', 'Coca'),
        ('Energie', 'Energie'),
        ('Maltina', 'Maltina'),
        ('Sprite', 'Sprite'),
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
    ])
    nom_conjoint = models.CharField(max_length=100, blank=True, null=True)
    prenom_conjoint = models.CharField(max_length=100, blank=True, null=True)
    boisson_conjoint = models.CharField(max_length=50, choices=[
       ('fanta', 'Fanta'),
        ('coca', 'Coca'),
        ('Energie', 'Energie'),
        ('Maltina', 'Maltina'),
        ('Sprite', 'Sprite'),
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
    ], blank=True, null=True)

    def __str__(self):
        return f"{self.prenom} {self.nom} {self.postnom}"