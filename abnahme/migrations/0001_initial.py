# Generated by Django 2.2.3 on 2019-07-26 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blatt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nummer', models.PositiveIntegerField(db_index=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('matr_nr', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('vorname', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentenGruppe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studenten', models.ManyToManyField(related_name='gruppen', to='abnahme.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Betreuer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('vorname', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Aufgabe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nummer', models.PositiveIntegerField(db_index=True, unique=True)),
                ('blatt', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='abnahme.Blatt')),
            ],
        ),
        migrations.CreateModel(
            name='Abnahme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('erfolgreich', models.BooleanField(default=False)),
                ('kommentar', models.TextField(blank=True)),
                ('aufgabe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abnahme.Aufgabe')),
                ('betreuer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='abnahme.Betreuer')),
                ('gruppe', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='abnahme.StudentenGruppe')),
            ],
        ),
    ]
