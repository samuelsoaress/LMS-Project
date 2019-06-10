from django.contrib import admin
from lms_app.professor import Professor 
from lms_app.disciplina import Disciplina
from lms_app.disciplinaofertada import DisciplinaOfertada

admin.site.register(Professor)
admin.site.register(Disciplina)
admin.site.register(DisciplinaOfertada)