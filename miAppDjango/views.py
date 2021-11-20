from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from miAppDjango.serializers import PersonaSerializer
from .models import Persona
from .serializers import  PersonaSerializer
from rest_framework import  serializers, viewsets

def index(request):
    """ return HttpResponse("MI PRIMERA PAGINA EN DJNAGO") """
    """ salida = ', '.join([ p.nombre for p in personas]) 
    return HttpResponse(salida)  """

    personas =Persona.objects.order_by('nombre')
    context = {
        'lista_pagina': 'Lista de personas',
        'lista_personas': personas,
        }
    return render(request, 'personas.html', context)
    
    
def detail(request, persona_id):
    persona =Persona.objects.get(pk=persona_id)
    context={
        'titulo_pagina':'Ver Persona',
        'persona':persona,
    }
    return render(request,'persona.html',context)

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class =PersonaSerializer