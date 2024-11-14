def seila(teste, *valores):
    print("-----teste-----")
    for param in valores:
        print(param)

def exibe(lista,titulo):
    lista.sort()
    print('------------------------')
    print('     ', titulo, '     ')
    print('------------------------')
    for nome in lista:
        print(nome)

def rect(x1 = 0,y1 = 0,x2 = 10,y2 = 10):
    print (x1,",",y1,",",x2,",",y2)

def media(n,m):
    """calcula a media de dois numeros"""
    return float(n+m)/2