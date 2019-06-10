from django.db import models
from .models import *
from lms_app.professor import *
from lms_app.disciplina import *

class DisciplinaOfertada(models.Model):
    curso = models.TextField(max_length=255)
    turma = models.TextField(max_length=5)
    ano = models.IntegerField() #um inteiro, representa um ano
    semestre = models.IntegerField() #um inteiro, 1 para primeiro sem e 2 para segundo
    professor = models.IntegerField() #id de um professor valido
    disciplina = models.IntegerField() #id de uma disciplina valid
    
    def save(self):
       
        if((len(DisciplinaOfertada.objects.filter(ano=self.ano))>0) and (len(DisciplinaOfertada.objects.filter(semestre=self.semestre))>0) and (len(DisciplinaOfertada.objects.filter(curso=self.curso))>0) and (len(DisciplinaOfertada.objects.filter(disciplina=self.disciplina))>0) and (len(DisciplinaOfertada.objects.filter(turma=self.turma))>0) and (len(DisciplinaOfertada.objects.filter(professor=self.professor))>0)):
                raise Exception('ERRO-9')
            
        if(self.curso not in ['ADS','SI','BD']): 
                raise Exception('EReRO')
           
    
       
        prof = Professor()
        professores_com_login = Professor.objects.filter(id=self.professor)
        
        disc = Disciplina()
        discplina_com_id = Disciplina.objects.filter(id=self.disciplina)
        if (len(professores_com_login) < 1):
            raise Exception('Erro')
      
        if (len(discplina_com_id) < 1): 
            raise Exception('Erro')
        
        super(DisciplinaOfertada,self).save()
            
        #print("SEM LOGIN")
        
           
