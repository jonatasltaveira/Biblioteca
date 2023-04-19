from django.contrib import admin
from .models import Usuario

# Register your models here.
admin.site.register(Usuario)
#@admin.register(Usuario)
#class UsuarioAdmin(admin.ModelAdmin):
#    readonly_fields = ('nome', 'email' 'senha') #impedirar que o ADM altere os dados do usuário
