from django.db import models
class Disciplina(models.Model):
    nome = models.TextField(max_length=50)
    ementa = models.TextField(max_length=5000)

    def save(self):
        if(len(Disciplina.objects.filter(nome=self.nome))>0):
            raise Exception('EReRO')
        #print("SEM LOGIN")
        super(Disciplina,self).save()
