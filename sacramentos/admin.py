# -*- coding:utf-8 -*-

from django.contrib import admin
from django.conf import settings
from django.contrib.auth.models import User, Permission
from django.contrib.auth.admin import UserAdmin

from .models import (
PerfilUsuario,
Libro, Bautismo, Eucaristia, Confirmacion, Matrimonio, NotaMarginal,
Intencion,
Parroquia, Iglesia, Direccion, 
AsignacionParroquia,
PeriodoAsignacionParroquia,
ParametrizaDiocesis,ParametrizaParroquia,
)
# def user_unicode(self):
#    	return  u'%s %s' % (self.first_name, self.last_name)

# User.__unicode__ = user_unicode
# admin.site.unregister(User)
# admin.site.register(User)
from sacramentos.models import Agenda


class LibroAdmin(admin.ModelAdmin):
	# fields = ('nombre', 'numero_libro', 'tipo_libro', 'fecha_apertura')
	list_display = ('nombre', 'numero_libro', 'tipo_libro', 'fecha_apertura')
	search_fields = ('nombre', 'numero_libro', 'tipo_libro', 'fecha_apertura')
	list_per_page = 20



admin.site.register(AsignacionParroquia)
admin.site.register(Bautismo)
admin.site.register(Confirmacion)
admin.site.register(Eucaristia)
admin.site.register(Intencion)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Matrimonio)
admin.site.register(NotaMarginal)
admin.site.register(Parroquia)
admin.site.register(Iglesia)
admin.site.register(ParametrizaDiocesis)
admin.site.register(ParametrizaParroquia)
admin.site.register(PerfilUsuario)
admin.site.register(PeriodoAsignacionParroquia)
admin.site.register(Permission)
admin.site.register(Agenda)

