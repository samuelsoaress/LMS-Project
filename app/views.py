from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.models import *
from app.forms import *
from django.core.mail import send_mail
from django_get_started.settings import EMAIL_HOST_USER

def index(request):

    context = {
        
        "User" : Aluno.objects.all()
        
    }
    return render(request, "index.html")

def contato(request):
    form = ContatoForm(request.POST)
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    telefone = request.POST.get('telefone')
    assunto = request.POST.get('assunto')
    conteudo_mensagem = request.POST.get('mensagem')
    mensagem = "Nome: {}. Telefone: {}. Mensagem: {}".format(nome, telefone, conteudo_mensagem)
    emailOrigem = EMAIL_HOST_USER

    #send_mail(assunto, mensagem, emailOrigem, emailDestino, fail_silently=True)
    send_mail(assunto, mensagem, emailOrigem , [email])
    
    context = { "contato" : form }
    return render(request, "contato.html" , context)

def cursos(request):
    form = Contato()
    context = { "cursos.html" : form,
                "lista_cursos": Cursos.objects.all() }
    return render(request, "cursos.html" , context)    
    
def inscricao(request):
    form = Contato()
    context = {"inscricao.html" : form }
    return render(request, "inscricao.html" , context)

def logado(request):
    form = ContatoForm()
    context = {"inscricao.html" : form }
    return render(request, "logado.html" , context)  


def disciplinas(request):
    form = Contato()
    context = {"disciplinas.html" : form }
    return render(request, "disciplinas.html" , context)

def restrito(request):
    turma = Turma.objects.all()
    for turmas in turma:
        turma.questoes = Questao.objects.filter(turma=turma)
    context = { "turmas":turmas }

    return render(request, "restrito.html" , context)

def questao_form(request, numero, questao_id=None):
    turma = Turma.objects.get(sigla=sigla)

    if questao_id:
        questao = Questao.objects.get(id=questao_id)
    else:
        questao = Questao(curso=curso)
        
    if request.POST:
        form = QuestaoForm(request.POST, request.FILES, instance=questao)
        if form.is_valid():
            form.save()
            return redirect("/restrito.html")
    else:   
        form = QuestaoForm(instance=questao)
    context = { 
        "form" : form,
        "curso" : Curso 
    }
    return render(request,"questao_form.html",context)

def newQuestionForm(id,question):
    turma = Turma.objects.get(question)
    return Turma(form)

