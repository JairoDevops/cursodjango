from django.contrib import admin
from .models import AutorDB, FraseDB, ProfesionDB


admin.site.site_header= "administracion"
admin.site.index_title = "crear"

@admin.register(ProfesionDB)
class ProfesionAdmin(admin.ModelAdmin):
    list_display = ['nombre'] 
    fields = ['nombre'] 


class AuthorAdmin(admin.ModelAdmin):
    fields = ['nombre', 'fecha_nacimiento', 'fecha_fallecimiento', ]  
    list_display = ['nombre', 'fecha_nacimiento', ] 
        
    def actualizar_o(self, request, queryset):
        for obj in queryset:
            if "O" in obj.nombre:
                nombre1= obj.nombre
                obj.nombre = nombre1.replace("O","o")
                obj.save()
                self.message_user(request,"exito")
    actualizar_o.short_description = "actualizar laletras 0"

    actions = ['actualizar_o']

admin.site.register(AutorDB, AuthorAdmin)

@admin.register(FraseDB)
class FraseAdmin(admin.ModelAdmin):
    fields =["frase", "autor_fk"]
    list_display = ["frase"] 