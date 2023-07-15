from django.contrib import admin

# Register your models here.
from .models import Kayit
from .models import Kayit


class KayitAdmin(admin.ModelAdmin):
    list_display = ('isim','numara','konu','aciklama','durumu')
    list_editable = ('durumu')



admin.site.register(Kayit, KayitAdmin)




