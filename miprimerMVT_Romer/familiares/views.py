from django.shortcuts import render
from familiares.models import Familiares

def nuevo_familiar(request):
    familiar_1 = Familiares.objects.create(dni= 20890398,nombre='Pablo',apellido='Römer',fecha_nacimiento='1978-12-19',parentesco='Padre',rama_familiar='Paterna')
    familiar_2 = Familiares.objects.create(dni= 23909409,nombre='Susana',apellido='Segura',fecha_nacimiento='1980-4-20',parentesco='Madre',rama_familiar='Materna')
    familiar_3 = Familiares.objects.create(dni= 33138903,nombre='Martín',apellido='Römer',fecha_nacimiento='1989-11-01',parentesco='Hermano')
    familiar_4 = Familiares.objects.create(dni= 5678019,nombre='Beatriz',apellido='Römer',fecha_nacimiento='1940-10-25',parentesco='Abuela',rama_familiar='Materna')
    
    lista_familiares = {
        'familiares_creados':[familiar_1,familiar_2,familiar_3,familiar_4]
    }

    return render(request,'familiar_nuevo.html',context=lista_familiares)

def familia_entera(request):
    familiares_totales = Familiares.objects.all()
    context = {
        'familiares_totales':familiares_totales
    }
    return render(request,'familia_entera.html',context=context)