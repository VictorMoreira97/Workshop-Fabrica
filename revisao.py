#REVISÃO - PYTHON - O ESSENCIAL
#Funções básicas Python: def nome_da_função(), tudo que estiver na hierarquia será executado quanod a função for chamada
def escrever_na_tela():
    print('Hello World')
def soma_num(n1, n2):
    return n1 + n2

#comando
escrever_na_tela()
n1=int(input("Digite um número "))
n2=int(input("Digite um número: "))
soma = soma_num(n1, n2)
print(soma)

#funções com argumentos
#   def nome_da_funcao(*args)
#   os argumentos servem para quando não se sabe a quantidade de parâmetros

#POO
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('João', 20)
print(p1.nome)
print(p1.idade)

