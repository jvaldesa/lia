from django.contrib import admin
from .models import Municipio, Estado, TipoAnalisis, Organizacion, RegimenHidrico, Cultivo, Analista

# Register your models here.
class EstadoAdmin(admin.ModelAdmin):
    pass

class MunicipioAdmin(admin.ModelAdmin):
   list_display = ('nombre', 'estado')
   search_fields= ('nombre',)
   list_filter = ('estado',)

class TipoAnalisisAdmin(admin.ModelAdmin):
   pass

class OrganizacionAdmin(admin.ModelAdmin):
   readonly_fields = ('created', 'updated')

class RegimenHidricoAdmin(admin.ModelAdmin):
   pass

class CultivoAdmin(admin.ModelAdmin):
   pass

admin.site.register(Estado, EstadoAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(TipoAnalisis, TipoAnalisisAdmin)
admin.site.register(Organizacion, OrganizacionAdmin)
admin.site.register(RegimenHidrico, RegimenHidricoAdmin)
admin.site.register(Cultivo, CultivoAdmin)
admin.site.register(Analista)
