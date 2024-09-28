from django.contrib import admin
from .models import Dados, Cultivo, Usuario

# Registro da página de admin
admin.site.register(Dados)
admin.site.register(Cultivo)
admin.site.register(Usuario)
