from django.contrib import admin
from django.urls import path
from miprimerMVT_Romer.views import consigna
from familiares.views import nuevo_familiar,familia_entera

urlpatterns = [
    path('admin/', admin.site.urls),
    path('consigna_MVT/',consigna,name='consigna_MVT'),
    path('nuevo_familiar/',nuevo_familiar,name='nuevo_familiar'),
    path('familia_entera/',familia_entera,name='familia_entera')
]
