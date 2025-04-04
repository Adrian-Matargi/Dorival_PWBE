from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioDS16

class UsuarioDS16Admin(UserAdmin):
    list_display = ('username', 'email', 'data_nascimento', 'edv', 'padrinho', 'apelido')

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('data_nascimento', 'edv', 'padrinho', 'apelido')}),
    )
   
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('data_nascimento', 'edv', 'padrinho', 'apelido')}),
    )

admin.site.register(UsuarioDS16, UsuarioDS16Admin)