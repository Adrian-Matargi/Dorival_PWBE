from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioDS16

class UsuarioDS16Admin(UserAdmin):
    list_display = ('username', 'biografia', 'idade', 'telefone', 'endereco', 'escolaridade', 'animais')

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('biografia', 'idade', 'telefone', 'endereco', 'escolaridade', 'animais')}),
    )
   
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('biografia', 'idade', 'telefone', 'endereco', 'escolaridade', 'animais')}),
    )

admin.site.register(UsuarioDS16, UsuarioDS16Admin)