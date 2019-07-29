from django.db import models
from django.conf import settings


class Student(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    matr_nr = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    vorname = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.vorname} {self.name} ({self.matr_nr})"


class StudentenGruppe(models.Model):
    studenten = models.ManyToManyField(Student, related_name='gruppen')

    def __str__(self):
        return f"Gruppe {self.id} (" + ", ".join(str(student) for student in self.studenten.all()) + ")"
    # TODO created_at = models.DateTimeField()


class Blatt(models.Model):
    nummer = models.PositiveIntegerField(unique=True, db_index=True)

    def __str__(self):
        return f"Blatt {self.nummer}"


class Aufgabe(models.Model):
    nummer = models.PositiveIntegerField(unique=True, db_index=True)
    blatt = models.ForeignKey(Blatt, on_delete=models.PROTECT)

    def __str__(self):
        return f"Aufgabe {self.nummer}, {self.blatt}"


class Betreuer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    vorname = models.CharField(max_length=255)

    def __str__(self):
        return f"Betreuer {self.vorname} {self.name}"


class Abnahme(models.Model):
    gruppe = models.ForeignKey(StudentenGruppe, on_delete=models.PROTECT)
    betreuer = models.ForeignKey(Betreuer, on_delete=models.PROTECT)
    aufgabe = models.ForeignKey(Aufgabe, on_delete=models.CASCADE)
    erfolgreich = models.BooleanField(default=False)
    kommentar = models.TextField(blank=True)

    def __str__(self):
        return f"Abnahme für {self.gruppe} von {self.betreuer}{' (erfolglos)' if not self.erfolgreich else ''}"
