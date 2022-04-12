from multiprocessing import context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_list_or_404, render
from django.urls import reverse

from .models import Region, Candidato
# Create your views here.

def index(request):
    lista_regiones = Region.objects.all()
    context = {
        'lista_regiones':lista_regiones
    }
    return render(request,'eleccionesRegional/index.html',context)

def list_candidates(request, region_id):
    lista_candidatos = Candidato.objects.filter(region_id=region_id)
    context = {
        'lista_candidatos':lista_candidatos
    }
    return render(request,'eleccionesRegional/candidatos.html',context)

