from django.db import models
from .models import *
from lms_app.professor import *

class Aluno(models.Model):

    nome = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    celular = models.TextField(max_length=20)
    login = models.TextField(max_length=20)
    senha = models.TextField(max_length=20)

    def save(self):
        if (self.email==''):
            self.email='email nao fornecido'

        if (self.login==''):
           raise Exception('login não fornecido')
        
           prof = Professor()
        professor_login  = Professor.objects.filter(login=self.login)
        if (len(professor_login) > 0):
            raise Exception('login ja utilizado por um professor')

        alunos_com_login = Aluno.objects.filter(login=self.login)
        if len(alunos_com_login) > 0:
            raise Exception('login ja utilizado por um aluno')

     

        super(Aluno,self).save()
