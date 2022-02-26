from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Pet, Vaccine

def home(request):
   pets = Pet.objects.all
   return render(request, 'adoptions/home.html', {'pets': pets})

def pet_detail(request, id):
   pet = get_object_or_404(Pet, pk=id)
   return render(request, 'adoptions/pet_detail.html', {'pet': pet})
