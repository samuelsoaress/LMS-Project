from django.test import TestCase
from .models import *

# Create your tests here.
class ProfessorTests(TestCase):
    '''
    Isso nao é um teste. Pode ignorar
    '''
    def setUp(self):
        professor = Professor()
        professor.login='astro'
        professor.save()
        professor = Professor()
        professor.login='segundo'
        professor.save()
        try:
           disciplina = Disciplina()
        except:
           return
        disciplina = Disciplina()
        disciplina.nome = 'Agronomia'
        disciplina.save()
        
    '''
    Testa os campos que o professor tem que ter.

    O teste salva o professor e depois verifica se salvou mesmo
    '''    
    def test_01_criar_professor(self):
        professor = Professor()
        professor.email='lucas@provedor.com'
        professor.nome='lucas'
        professor.celular='99999'
        professor.login='lucas'
        professor.senha='lucas123'
        professor.save()
        resultados=Professor.objects.filter(nome='lucas')
        resultado = resultados[0]
        self.assertEqual(resultado.login,'lucas')
        self.assertEqual(resultado.celular,'99999')
        self.assertEqual(resultado.nome,'lucas')
        self.assertEqual(resultado.email,'lucas@provedor.com')
        self.assertEqual(resultado.senha,'lucas123')


        
    '''
    devemos ter uma exception quando o professor vier sem login    
    '''
    def test_02_sem_login(self):
        professor = Professor()
        professor.nome='lucas'
        professor.celular='99999'
        professor.senha='lucas123'
        self.assertRaises(Exception,professor.save)

    '''
    quando criamos um professor sem email, seu email deve ser 
    a string 'email nao fornecido'

    O teste salva um professor sem email, carrega e verifica se ele vem
    com essa string no campo email
    '''
    def test_03_sem_email(self):
        professor = Professor()
        professor.nome='lucas'
        professor.celular='99999'
        professor.login='lucas'
        professor.senha='lucas123'
        professor.save()
        resultados=Professor.objects.filter(nome='lucas')
        resultado = resultados[0]
        self.assertEqual(resultado.email,'email nao fornecido')
        self.assertEqual(len(resultados),1)


    '''
    Devemos ter uma exception se o professor está vindo com um login que já existe
    '''
    def test_04_login_repetido(self):
        professor = Professor()
        professor.login='lucas'
        professor.save()
        professor = Professor()
        professor.login='lucas'
        self.assertRaises(Exception,professor.save)

    '''
    Os campos que deve ter uma disciplina

    O teste salva e carrega pra ver se esta OK
    '''
    def test_05_disciplina_salvar(self):
        disciplina = Disciplina()
        disciplina.nome = 'Matematica'
        disciplina.ementa = 'resolver equacoes'
        disciplina.save()
        disciplinas = Disciplina.objects.filter(nome='Matematica')
        disciplina_resultante = disciplinas[0]
        self.assertEqual(disciplina_resultante.ementa, 'resolver equacoes')

    '''
    Nao pode haver duas disciplinas com o mesmo nome
    Se tentarmos salvar a segunda com o nome, deve ocorrer uma exception
    ''' 
    def test_06_disciplina_dobrada(self):
        disciplina = Disciplina()
        disciplina.nome = 'Matematica'
        disciplina.save()
        disciplina2 = Disciplina()
        disciplina2.nome = 'Matematica'
        self.assertRaises(Exception,disciplina2.save)

    '''
    Uma disciplinaOfertada é uma turma. Disciplina seria, por exemplo, lp2
    disciplinaOfertada, lp2 no segundo semeste de 2018 para o curso de ADS
    Veja os campos de uma disciplina ofertada abaixo
    '''
    def test_07_ofertada_salvar(self):
        ofertada = DisciplinaOfertada()
        ofertada.curso='ADS'
        ofertada.ano=2018
        ofertada.semestre=2
        ofertada.turma='2a'
        ofertada.professor=1
        ofertada.disciplina=1
        ofertada.save()
        ofertada = DisciplinaOfertada()
        ofertada.curso='ADS'
        ofertada.ano=2018
        ofertada.semestre=1
        ofertada.turma='2a'
        ofertada.professor=1
        ofertada.disciplina=1
        ofertada.save()
        ofertada = DisciplinaOfertada()
        ofertada.curso='SI'
        ofertada.ano=2018
        ofertada.semestre=2
        ofertada.turma='2a'
        ofertada.professor=1
        ofertada.disciplina=1
        ofertada.save()
        ofertada = DisciplinaOfertada()
        ofertada.curso='ADS'
        ofertada.ano=2017
        ofertada.semestre=2
        ofertada.turma='2a'
        ofertada.professor=1
        ofertada.disciplina=1
        ofertada.save()
        ofertada = DisciplinaOfertada()
        ofertada.curso='ADS'
        ofertada.ano=2017
        ofertada.semestre=2
        ofertada.turma='2b'
        ofertada.professor=1
        ofertada.disciplina=1
        ofertada.save()
        ofertas = DisciplinaOfertada.objects.filter(curso='ADS')
        self.assertEqual(len(ofertas),4)
        ofertas = DisciplinaOfertada.objects.filter(curso='SI')
        self.assertEqual(len(ofertas),1)
        self.assertEqual(Professor.objects.get(id=1).login,'astro')
        self.assertEqual(Disciplina.objects.get(id=1).nome,'Agronomia')


    '''
    O campo curso pode ter 3 valores distintos: 'ADS', 'SI' e 'BD'

    Se passarmos algum outro, o codigo deve dar uma exception
    '''
    def test_08_ofertada_salvar_curso_invalido(self):
        ofertada = DisciplinaOfertada()
        ofertada.curso='MAT'
        ofertada.ano=2018
        ofertada.semestre=2
        ofertada.turma='2a'
        ofertada.professor=1
        ofertada.disciplina=1
        self.assertRaises(Exception,ofertada.save)

    '''
    Não podemos criar duas ofertadas com o mesmo ano. semestre, turma, curso e disciplina
    Alguma dessas coisas tem que variar

    Se tentarmos salvar uma disciplina "repetida" com todos os dados
    iguais, devemos ter uma exception

    '''
    def test_09_ofertada_repetida(self):
        ofertada = DisciplinaOfertada()
        ofertada.curso='ADS'
        ofertada.ano=2018
        ofertada.semestre=2
        ofertada.turma='2a'
        ofertada.professor=1
        ofertada.disciplina=1
        ofertada.save()
        ofertada = DisciplinaOfertada()
        ofertada.curso='ADS'
        ofertada.ano=2018
        ofertada.semestre=2
        ofertada.turma='2a'
        ofertada.professor=1
        ofertada.disciplina=1
        self.assertRaises(Exception,ofertada.save)

    '''
    Temos que tomar cuidado para usarmos Ids válidas de professor e de disciplina, ao definir uma
    disciplinaOfertada

    Se dermos uma id inválida de professor ou de disciplina, devemos dar uma exception
    
    O codigo salva uma disciplina ofertada invalida, com ids invalidas
    para verificar a exception.

    Depois salva uma valida, para verificar que isso nao da exception
    '''
    def test_10_ofertada_mal_definida_prof_ou_disciplina(self):
        ofertada = DisciplinaOfertada()
        ofertada.curso='ADS'
        ofertada.ano=2018
        ofertada.semestre=2
        ofertada.turma='2a'
        ofertada.professor=100
        ofertada.disciplina=1
        self.assertRaises(Exception,ofertada.save)
        ofertada.professor=1
        ofertada.disciplina=100
        self.assertRaises(Exception,ofertada.save)
        ofertada.professor=2
        ofertada.disciplina=1
        try:
           ofertada.save()
        except Exception:
            self.fail("fiz uma ofertada valida mas recebi exception")
    
    '''
    Aluno é um modelo igual ao professor
    '''
    def test_11_criar_aluno(self):
        aluno = Aluno()
        aluno.email='lucas@provedor.com'
        aluno.nome='lucas'
        aluno.celular='99999'
        aluno.login='lucas'
        aluno.senha='lucas123'
        aluno.save()
        resultados=Aluno.objects.filter(nome='lucas')
        resultado = resultados[0]
        self.assertEqual(resultado.login,'lucas')
        self.assertEqual(resultado.celular,'99999')
        self.assertEqual(resultado.nome,'lucas')
        self.assertEqual(resultado.email,'lucas@provedor.com')
        self.assertEqual(resultado.senha,'lucas123')
    '''
    Que também nao aceita ficar sem email, e troca para
    'email nao fornecido'
    '''
    def test_12_sem_email(self):
        professor = Aluno()
        professor.nome='lucas'
        professor.celular='99999'
        professor.login='lucas'
        professor.senha='lucas123'
        professor.save()
        resultados=Aluno.objects.filter(nome='lucas')
        resultado = resultados[0]
        self.assertEqual(resultado.email,'email nao fornecido')
        self.assertEqual(len(resultados),1)
        
    '''
    Também dá erro sem login
    '''

    def test_13_sem_login(self):
        aluno = Aluno()
        aluno.nome='lucas'
        aluno.celular='99999'
        aluno.senha='lucas123'
        self.assertRaises(Exception,aluno.save)

    '''
    E tem erro com login repetido
    '''
    def test_14_login_repetido(self):
        aluno = Aluno()
        aluno.login='lucas'
        aluno.save()
        aluno = Aluno()
        aluno.login='lucas'
        self.assertRaises(Exception,aluno.save)

    '''
    Se o professor escolheu um login, o aluno nao pode escolher
    '''
    def test_15_login_repetido_professor_atrapalha_aluno(self):
        professor = Professor()
        professor.login='lucas'
        professor.save()
        aluno = Aluno()
        aluno.login='lucas'
        self.assertRaises(Exception,aluno.save)

    '''
    E se o aluno escolher, o professor nao pode
    '''
    def test_16_login_repetido_aluno_atrapalha_professor(self):
        aluno = Aluno()
        aluno.login='lucas'
        aluno.save()
        professor = Professor()
        professor.login='lucas'
        self.assertRaises(Exception,professor.save)

    '''
    Isso não é um teste
    '''
    def prepara_para_matricula(self):
        aluno = Aluno()
        aluno.login='power'
        aluno.save()
        disciplinas = []
        disciplinas.append(Disciplina())
        disciplinas[-1].nome = 'Portugues'
        disciplinas[-1].save()
        disciplinas.append(Disciplina())
        disciplinas[-1].nome = 'Ingles'
        disciplinas[-1].save()
        disciplinas.append(Disciplina())
        disciplinas[-1].nome = 'Espanhol'
        disciplinas[-1].save()
        disciplinas.append(Disciplina())
        disciplinas[-1].nome = 'Frances'
        disciplinas[-1].save()
        disciplinas.append(Disciplina())
        disciplinas[-1].nome = 'Japones'
        disciplinas[-1].save()
        for disciplina in disciplinas:
            ofertada = DisciplinaOfertada()
            ofertada.curso='ADS'
            ofertada.ano=2000
            ofertada.semestre=2
            ofertada.turma='2a'
            ofertada.professor=1
            ofertada.disciplina=disciplina.id
            ofertada.save()
        
        

    '''
    Uma matricula tem um campo aluno e um campo disciplina ofertada
    '''
    def test_17_matricula(self):
        self.prepara_para_matricula()
        matricula = Matricula()
        matricula.aluno = 1
        matricula.disciplinaOfertada = 1
        matricula.save()
        self.assertEqual(len(Matricula.objects.all()),1)

    '''
    Um aluno pode fazer 3 disciplinas, mas nao 4
    '''
    def test_18_tres_matriculas(self):
        self.prepara_para_matricula()
        for i in [1,2,3]:
            matricula = Matricula()
            matricula.aluno = 1
            matricula.disciplinaOfertada = i
            matricula.save()
        self.assertEqual(len(Matricula.objects.all()),3)
    '''
    Um aluno pode fazer 3 disciplinas, mas nao 4
    '''
    def test_19_quatro_matriculas(self):
        self.prepara_para_matricula()
        for i in [1,2,3]:
            matricula = Matricula()
            matricula.aluno = 1
            matricula.disciplinaOfertada = i
            matricula.save()
        self.assertEqual(len(Matricula.objects.all()),3)
        matricula = Matricula()
        matricula.aluno = 1
        matricula.disciplinaOfertada = 4
        self.assertRaises(Exception,matricula.save)
    '''
    Um aluno não pode fazer dois oferecimentos da mesma disciplina
    '''
    def test_20_disciplina_repetida(self):
        self.prepara_para_matricula()
        fr = Disciplina.objects.filter(nome='Frances')[0]
        ids = []
        for turma in '2b','2c':
            ofertada = DisciplinaOfertada()
            ofertada.curso='BD'
            ofertada.ano=2000
            ofertada.semestre=2
            ofertada.turma=turma
            ofertada.professor=1
            ofertada.disciplina=fr.id
            ofertada.save()
            ids.append(ofertada.id)
        matricula = Matricula()
        matricula.aluno = 1
        matricula.disciplinaOfertada = ids[0]
        matricula.save()
        matricula = Matricula()
        matricula.aluno = 1
        matricula.disciplinaOfertada = ids[1]
        self.assertRaises(Exception,matricula.save)