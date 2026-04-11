from django.contrib import admin
from .models import Licenciatura, UnidadeCurricular, Docente

admin.site.register(Licenciatura)
admin.site.register(Docente)
admin.site.register(UnidadeCurricular)

