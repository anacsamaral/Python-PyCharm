from Biblioteca.Modulo import *
import math

# MÉDIA
# def media(n,m):
#     """calcula a media de dois numeros"""
#     return float(n+m)/2
#

print (media(5,6))
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
print("A média é: ", media(n1, n2))
print("A função",media.__name__,media.__doc__)
help(media)

# FATORIAL
# def fatorial(numero):  #funcão recursiva
#     """
#     Funcao recursiva que retorna o valor do fatorial do numero
#     """
#     if numero <= 1:
#         return 1
#     else:
#         return (numero * fatorial (numero - 1 ))
#
# for n in range ( 1, 11 ):
#    print ('Fatori
#    al de %d é %d' %(n,fatorial(n)))
#
# print ('\nDoc. da função:\n',fatorial.__doc__)

# POTÊNCIA
# def potencia(base,exp=2):
#    """
#     Funcao que eleva um numero (base) a uma potencia (exp)
#     Caso nao seja informado o expoente, será considerado o expoente 2
#     """
#     if exp==0:
#        return 1
#    pot=base
#    i=1
#    while i < exp:
#       pot=pot*base
#       i=i+1
#    return pot
#
# print (potencia(2)) # imprime 4
# print (potencia(2,8)) #imprime 256

#RETÂNGULO
# função com parâmetros opcionais
# def rect(x1 = 0,y1 = 0,x2 = 10,y2 = 10):
#     print (x1,",",y1,",",x2,",",y2)
#
rect()
rect(5, 5, 8, 6)
rect(3, 4)
rect(x2 = 7)


rect()	                # imprime 0   0   10   10
rect(1,1)	    # imprime 1   1   10   10
rect(x2 = 100)           # imprime 0   0   100   10

# MÚLTIPLOS PARÂMETROS
def seila(teste, *valores):
    print("-----teste-----")
    for param in valores:
        print(param)

seila('Testando vários parâmetros', 'Cris', 'Carol','Chico', 'Cassia')

l_alunos = []
l_alunos.append('Ana')
l_alunos.append('Felipe')
l_alunos.append('Luis')
l_alunos.append('Otavio')

l_prof = []
l_prof.append('Cris')
l_prof.append('Chico')
l_prof.append('Leandro')
l_prof.append('Cezário')

# def exibe(lista,titulo):
#     lista.sort()
#     print('------------------------')
#     print('     ', titulo, '     ')
#     print('------------------------')
#     for nome in lista:
#         print(nome)

exibe(l_alunos,'Alunos Fofinhos')
exibe(l_prof,'Profs Maravilhosos')
