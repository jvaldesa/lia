from django.contrib import admin
from .models import Recepcion

# Register your models here.
class RecepcionAdmin(admin.ModelAdmin):
   list_display = ('folio', 'productor', 'estado')

admin.site.register(Recepcion, RecepcionAdmin)
