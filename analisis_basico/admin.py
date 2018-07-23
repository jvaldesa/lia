from django.contrib import admin
from .models import Textura, Ph_ConductividadElectrica, MateriaOrganica, ColorDensidadAparente, PuntoSaturacion
# Register your models here.
class TexturaAdmin(admin.ModelAdmin):
    pass

class PhCEAdmin(admin.ModelAdmin):
    pass

class MateriaOrganicaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Textura, TexturaAdmin)

admin.site.register(Ph_ConductividadElectrica, PhCEAdmin)

admin.site.register(MateriaOrganica, MateriaOrganicaAdmin)

admin.site.register(ColorDensidadAparente)

admin.site.register(PuntoSaturacion)
