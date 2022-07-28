from django.http import HttpResponse
from django.shortcuts import render

def consigna(request):
    tarea = {
        'tarea': 'Consigna: Crear una web que permite ver los datos de algunos de tus familiares, guardados en un BD.',
        'requisito_1': '1.Deberá tener un template, una vista y un modelo (como mínimo, pueden usar más).',
        'requisito_2' : '2.La clase del modelo, deberá guardar mínimo un número, una cadena y una fecha (puede guardar más cosas).',
        'requisito_3' : '3.Se deberán crear como mínimo 3 familiares.',
        'requisito_4' : '4.Los familiares se deben ver desde la web.'
    }
    return render(request,'consigna.html',context=tarea)