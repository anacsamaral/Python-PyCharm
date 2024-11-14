#for (start, stop - 1, step)
# print("======= range =======")
# print(list(range(0,10)))
#
# for i in range(0,10):
#     print (i)
#
# lista = ["banana", "maçã", "uva"]
# print(lista)
#
# for fruta in lista:
#     print("Fruta é uma " + fruta)
#
# print("======= try e except =======") #para não exibir o erro para o usuário, mostra a mensagem do except
# nome = 'Ana'
# try:
#     numero = int(nome)
#     print(numero)
# except:
#     print('Inválido!!! Não se transforma palavra em inteiro')
#
# print("======= Percorrer a lista pegando cada item durante a interação =======")
# lista = list(range(1,11))
# print(lista)
#
# pos = 0;
# for i in lista:
#     if i%2 == 0:
#         print('Lista[',pos,'] = ',i)
#     pos += 1
#
# print("=========================================")
# #percorrendo a lista pelo indice
# for i in range(1, len(lista), 2):
#     print('lista[',i,']=', lista[i])
#
# print("=========================================")
# print(lista[1::2])
#
# print("=========================================")
# lista = ['Carol', 'Cris', 'Chico']
# print(lista)
# listaInicial = lista #não copiou, mas referenciou o local de memória
# print(listaInicial)
#
# lista.append('Cassia')
# print(lista)
# print(listaInicial)
# copiaLista = lista[:] #copia a lista literalmente
# copiaLista.append('Mario') #insere sempre no final da lista
# print(lista)
# print(lista)
# print(copiaLista)
# copiaLista.sort()
# print(copiaLista)
#
# copiaLista.remove('Mario')
# print(copiaLista)
#
# copiaLista.insert(2,'Leandro')


#DICIONÁRIO

amigo = {}
amigo['nome'] = 'Cris'
amigo['idade'] = '49'
amigo['altura'] = '1.7'
print(amigo)

amigo2 = {}
amigo2['nome'] = 'Chico'
amigo2['idade'] = '50'
amigo2['altura'] = '1.8'
print(amigo2)

listadeamigos = [] #Lista
listadeamigos.append(amigo) #inseri o dicionario na lista
listadeamigos.append(amigo2)
print(listadeamigos)

listadeamigos.append({'nome':'Ana', 'Idade': 30, 'altura': 1.6})
print(listadeamigos)

for migs in listadeamigos:
    print(migs['nome'], '-', migs['idade'])