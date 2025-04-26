from django.db import models

class Participant(models.Model):
    nom = models.CharField(max_length=100)
    postnom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    genre = models.CharField(max_length=10, choices=[
        ('couple', 'Couple'),
        ('singleton', 'Singleton'),
    ])

    def __str__(self):
        return f"{self.prenom} {self.nom} {self.postnom}"