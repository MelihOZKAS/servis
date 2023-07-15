from django.shortcuts import render,redirect,HttpResponse
from .form import KayitForm

import environ
import requests


env = environ.Env(DEBUG=(bool,False))
environ.Env.read_env()
# Create your views here.
def home(request):
    return render(request,"system/home.html")


def hakkimizda(request):
    return render(request,"system/hakkimizda.html")

def hizmetlerimiz(request):
    return render(request,"system/hizmetlerimiz.html")

def iletisim(request):
    if request.method == 'POST':
        form = KayitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            joined_message = "Arıza kaydı talebi geldi lütfen yardımcı olalım."
            url = f"https://api.telegram.org/bot{env('Telegram_Token')}/sendMessage?chat_id={env('Telegram_Chat_id')}&text={joined_message}"
            r = requests.get(url)
            return HttpResponse("Arıza Talebiniz Alınmıştır Çağrı Merkezimiz Sizi En Kısa Sürede Arayacaktır.")  # Başarılı işlem sonrası yönlendirilecek sayfa
        else:
            print(form.errors)  # Hataları konsola yazdır
            return HttpResponse(form.errors)


    else:
        form = KayitForm()

    return render(request,"system/iletisim.html",{'form': form})