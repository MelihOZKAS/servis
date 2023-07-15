from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request,"system/home.html")


def hakkimizda(request):
    return render(request,"system/hakkimizda.html")