from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class UsuarioManager(BaseUserManager):
      use_in_migrations = True
      def _create_user(self, ra, password, **extra_fields):
          if not ra:
              raise ValueError('RA precisa ser preenchido')
          user = self.model(ra=ra, **extra_fields)
          user.set_password(password)
          user.save(using=self._db)
          return user

      def create_user(self, ra, password=None, **extra_fields):
          return self._create_user(ra, password, **extra_fields)

      def create_superuser(self, ra, password, **extra_fields):
          return self._create_user(ra, password, **extra_fields)


class Usuario(AbstractBaseUser):
      nome = models.CharField(max_length=50)
      ra = models.IntegerField(unique=True)
      perfil = models.CharField(max_length=1, default='C')
      ativo = models.BooleanField(default=True)
      email = models.CharField(max_length=200)
      celular = models.IntegerField("Celular")

      USERNAME_FIELD = 'ra'
      REQUIRED_FIELDS = ['nome']

      objects = UsuarioManager()

      @property
      def is_staff(self):
	return self.perfil == 'C'

      def has_perm(self, perm, obj=None):
        return True
      
      def has_module_perms(self, app_label):
        return True
  
      def get_short_name(self):
        return self.nome
      
      def get_full_name(self):
        return self.nome

      def __unicode__(self):
        return unicode(self.nome)

class Curso(models.Model):
    sigla = models.CharField(primary_key=True,max_length=5)
    nome = models.CharField(unique=True,max_length=50)                  
    def __unicode__(self):
      	return unicode(self.nome)
      
class GradeCurricular(models.Model):
    ano = models.SmallIntegerField("Ano")
    semestre = models.CharField(max_length=1)
    curso = models.ForeignKey(Curso)
    def __unicode__(self):
      	return unicode(self.semestre)

class Periodo(models.Model):
    numero = models.IntegerField("Numero")
    gradecurricular = models.ForeignKey(GradeCurricular)

class Disciplina(models.Model):
    nome = models.CharField(max_length=240)
    carga_horaria = models.IntegerField("Carga_Horaria")
    teoria = models.DecimalField(max_digits=3, decimal_places=1)
    pratica = models.DecimalField(max_digits=3, decimal_places=1)
    ementa = models.TextField(blank=True)
    competencias = models.TextField(blank=True)
    habilidades = models.TextField(blank=True)
    conteudo = models.TextField(blank=True)
    bibliografia_basica = models.TextField(blank=True)
    bibliografia_complementar = models.TextField(blank=True)
    def __unicode__(self):
      	return unicode(self.nome)

class PeriodoDisciplina(models.Model):
    gradecurricular = models.ForeignKey(GradeCurricular)
    disciplina = models.ForeignKey(Disciplina)
      
class DisciplinaOfertada(models.Model):
    ano = models.SmallIntegerField("Ano")
    semestre = models.CharField(max_length=1)
    disciplina = models.ForeignKey(Disciplina)
    def __unicode__(self):
      	return unicode(self.semestre)

class Aluno(Usuario):

    curso = models.ForeignKey(
        Curso
    )

class Professor(Usuario):
    apelido = models.CharField(unique=True,max_length=30)
      
class Turma(models.Model):
    turma = models.CharField(max_length=15)
    disciplina = models.ForeignKey(Disciplina)
    disciplinaOfertada = models.ForeignKey(DisciplinaOfertada)
    professor = models.ForeignKey(Professor)
    def __unicode__(self):
      	return unicode(self.turma)
      
class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno)
    turma = models.ForeignKey(Turma)
      
class CursoTurma(models.Model):
    curso = models.ForeignKey(Curso)
    turma = models.ForeignKey(Turma)
      
class Questao(models.Model):
    numero = models.IntegerField("Numero")
    data_limite_entrega = models.DateField(auto_now=False, auto_now_add=False)
    descricao = models.TextField(blank=True)
    data = models.DateField(auto_now=False, auto_now_add=False)
    turma = models.ForeignKey(Turma)

def arquivosQ(arquivosquestao, nome_arquivo):
      return "{}/{}/{}".format(arquivosquestao.questao.numero, arquivosquestao.numero_questao, nome_arquivo)
      
class ArquivosQuestao(models.Model):
    numero_questao = models.IntegerField("NumeroQuestao")
    arquivo = models.FileField(upload_to="arquivosQ")
    questao = models.ForeignKey(Questao)

class Resposta(models.Model):
    questao = models.ForeignKey(Questao)
    aluno = models.ForeignKey(Aluno)
    data_avaliacao = models.DateField(auto_now=False, auto_now_add=False)
    nota = models.DecimalField(max_digits=4, decimal_places=2)
    avaliacao = models.TextField(blank=True)
    descricao = models.TextField(blank=True)
    data_de_envio = models.DateField(auto_now=False, auto_now_add=False)
      
class ArquivosResposta(models.Model):
    resposta = models.ForeignKey(Resposta)      
    arquivo = models.FileField(upload_to="arquivosR/")
	
