# Generated by Django 3.2.25 on 2024-08-22 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('PINTURA', 'Pintura'), ('ESCULTURA', 'Escultura'), ('FOTOGRAFIA', 'Fotografia'), ('DESENHO', 'Desenho'), ('ARTE DIGITAL', 'Arte Digital'), ('INSTALAÇÃO', 'Instalação'), ('ARTE ABSTRATA', 'Arte Abstrata'), ('ARTE CONTEMPORÂNEA', 'Arte Contemporânea'), ('ARTE CLÁSSICA', 'Arte Clássica'), ('ARTE URBANA', 'Arte Urbana')], default='', max_length=100),
        ),
    ]
