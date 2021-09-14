from django.contrib import admin
from .models import Chassi, Carro


@admin.register(Chassi)
class ChassiAdmin(admin.ModelAdmin):
    # lista display sempre espera uma tupla, por isso usei a virgula.
    list_display = ('numero',)


@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'chassi', 'preco')