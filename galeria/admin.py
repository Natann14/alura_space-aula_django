from django.contrib import admin
from galeria.models import Fotografia

# silas; admin123
# Register your models here.

class ListandoFotografias(admin.ModelAdmin):
    # Listando o que queremos que apareca no django admin
    list_display = ("id", "nome", "legenda")
    list_display_links = ("id", "nome")
    search_fields = ("nome", )
    
admin.site.register(Fotografia, ListandoFotografias)
