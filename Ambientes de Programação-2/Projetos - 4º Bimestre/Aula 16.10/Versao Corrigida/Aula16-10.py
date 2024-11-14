from Biblioteca.Modulo import *
import math
#import Biblioteca.Modulo as Bib
print('A média é: ', media(7,6))
med = media(2,8)
print('A média é: ', med)
n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
print('A média é: ', media(n1,n2))
print('A função',media.__name__,media.__doc__)
help(media)

math.cos(10)
rect()
rect(5,5,8,6)
rect(3,4)
rect(x2=7)



seila('Testando vários parâmetros','Cris', 'Carol','Chico','Cassia')

l_alunos=[]
l_alunos.append('Ana')
l_alunos.append('Felipe')
l_alunos.append('Luis')
l_alunos.append('Otavio')

l_prof=[]
l_prof.append('Cris')
l_prof.append('Chico')
l_prof.append('Leandro')
l_prof.append('Cezário')



exibe(l_alunos,'Alunos Fofinhos')
exibe(l_prof,'Professores Maravilhosos')