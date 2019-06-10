from django.db import models

class Professor(models.Model):
    def __str__(self):
        return self.nome + " " + self.email

    nome = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    celular = models.TextField(max_length=20)
    login = models.TextField(max_length=20)
    senha = models.TextField(max_length=20)

    def save(self):
        
        print('Estou Salvando')
        if(self.login==''):
            raise Exception('login não enviado')
        if (self.email==''):
            self.email='email nao fornecido'
            
        professores_com_login = Professor.objects.filter(login=self.login)
        if len(professores_com_login) > 0:
            raise Exception('login ja utilizado')
        #print("SEM LOGIN")
        super(Professor,self).save()