from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.views.generic import RedirectView
from django.contrib.auth.views import login,logout
from django.conf import settings
from django.conf.urls.static import static
from app.views import *

urlpatterns = [
    url(r'^$', login,{ 'template_name':'index.html' }),
    url(r'^contato.html', login,{ 'template_name':'contato.html' }),
    url(r'^logado.html', login,{ 'template_name':'logado.html' }),
    url(r'^disciplinas.html', login,{ 'template_name':'disciplinas.html' }),
    url(r'^inscricao.html', login,{ 'template_name':'inscricao.html' }),
    url(r'^admin/', admin.site.urls),
    url(r'^cursos.html', login,{ 'template_name':'cursos.html' }),   
    url(r'^tarefas_entregues.html', login,{ 'template_name':'tarefas_entregues.html' }),
    url(r'^index.html', login,{ 'template_name':'index.html' }),
    
    url(r'^restrito.html/$', restrito , name="restrito"),
    url(r'^questao_form.html/$', restrito , name="questao_form"),

    url(r'^questao_form.html/(?P<sigla>[A-Z,a-z]+)/questao/(?P<questao_id>[0-9]*)', questao_form , name="questao_form"),

    url(r'^cursos.html/([A-Z,a-z]+)',cursos),
    url(r'^sair/', logout , {'next_page': '/index.html'})
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
