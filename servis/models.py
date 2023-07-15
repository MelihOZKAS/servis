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
    GizliAciklama = models.TextField(blank=True,null=True)
    durumu = models.ForeignKey(DURUMU_CHOICES, related_name='Durum',default=BEKLEMEDE, blank=True, null=True,
                                   on_delete=models.SET_NULL)
    tarih = models.DateTimeField(auto_now_add=True)