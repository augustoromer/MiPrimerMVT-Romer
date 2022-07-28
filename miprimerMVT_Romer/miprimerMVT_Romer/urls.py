from django.contrib import admin
from django.urls import path
from miprimerMVT_Romer.views import consigna

urlpatterns = [
    path('admin/', admin.site.urls),
    path('consigna_MVT/',consigna,name='consigna_MVT'),
]
