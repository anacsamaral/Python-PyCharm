##Calcula a média
def media(a,b):
    '''Calcula a média de 2 notas'''
    m = (a+b)/2
    return m

#Função com parâmetros opcionais
def rect(x1=0,y1=0,x2=10,y2=10):
    print('Dimensão do retângulo: ',x1,',',y1,',',x2,',',y2)

#Multiplos parâmetros
def seila(teste,*valores):
    print('----',teste,'----')
    for param in valores:
        print(param)

def exibe(lista,titulo):
    lista.sort()
    print('--------------------')
    print('   ',titulo,'  ')
    print('--------------------')
    for nome in lista:
        print(nome)