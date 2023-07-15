from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name = "home"),
    path("hakkimizda/", views.hakkimizda, name='hakkimizda'),
    path("iletisim/", views.iletisim, name='iletisim'),

]
