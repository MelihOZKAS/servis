from django.db import models

# Create your models here.
BEKLEMEDE = 'Beklemede'
ISLEMDE = 'İşlemde'
BASARILI = 'Basarili'
Olumsuz = 'Olumsuz'

DURUMU_CHOICES = [
    (BEKLEMEDE, 'Beklemede'),
    (ISLEMDE, 'İşlemde'),
    (BASARILI, 'Basarili'),
    (Olumsuz, 'Olumsuz'),
]

class Kayit(models.Model):
    isim = models.CharField(max_length=255)
    numara = models.CharField(max_length=100)
    konu = models.CharField(max_length=100)
    aciklama = models.TextField(blank=True, null=True)
    durumu = models.CharField(max_length=10, choices=DURUMU_CHOICES, default=BEKLEMEDE, blank=True, null=True)
    tarih = models.DateTimeField(auto_now_add=True)