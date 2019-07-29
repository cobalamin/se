from django.contrib import admin

from .models import Betreuer, Student, StudentenGruppe, Blatt, Aufgabe, Abnahme

# Register your models here.
for model in [Betreuer, Student, StudentenGruppe, Blatt, Aufgabe, Abnahme]:
    admin.site.register(model)
