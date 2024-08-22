from django.db import models
from datetime import datetime

class Fotografia(models.Model):

    OPCOES_CATEGORIA = [
        ("PINTURA", "Pintura"),
        ("ESCULTURA", "Escultura"),
        ("FOTOGRAFIA", "Fotografia"),
        ("DESENHO", "Desenho"),
        ("ARTE DIGITAL", "Arte Digital"),
        ("INSTALAÇÃO", "Instalação"),
        ("ARTE ABSTRATA", "Arte Abstrata"),
        ("ARTE CONTEMPORÂNEA", "Arte Contemporânea"),
        ("ARTE CLÁSSICA", "Arte Clássica"),
        ("ARTE URBANA", "Arte Urbana")
    ]


    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now(), blank=False)

    def __str__(self):
        return self.nome