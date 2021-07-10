from django.contrib import admin
from django.contrib.admin.decorators import register
from app_banco.models import Cliente, Cuentas

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'telefono', 'correo',)


admin.site.register (Cliente, ClienteAdmin)

admin.site.register(Cuentas)
