from django.shortcuts import render, redirect
from formulaire.models import Etudiant
from .form import EtudiantForm


# Create your views here.

def formulaire(request):
   if request.method =='POST':
        form = EtudiantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
   else:
       form = EtudiantForm()
   return render(request,'formulaire/formulaire.html',{'form':form})


def success(request):
    return render(request,'formulaire/success.html')


def evenement(request):
    return render(request, 'formulaire/actualite.html')

def cours(request):
    return render(request,'formulaire/cours.html')

