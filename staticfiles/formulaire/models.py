from django.db import models

# Create your models here.

class Etudiant(models.Model):
    SEXE= (('MASCULIN','MASCULIN'),('FEMININ','FEMININ'))
    nom       = models.CharField(max_length=50, blank=False,null=True)
    prenom    = models.CharField(max_length=50, blank=False,null=True)
    classe    = models.CharField(max_length=50,blank=False,null=True)
    sexe      = models.CharField(max_length=50,blank=False,null=True, choices=SEXE)
    telephone = models.CharField(max_length=50,blank=True,null=True)
    email     = models.CharField(max_length=50,blank=True,null=True)
    date_creation =models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.nom

