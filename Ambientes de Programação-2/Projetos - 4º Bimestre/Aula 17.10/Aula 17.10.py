# # ARQUIVO DE TEXTO
#
# # arq = open('teste.txt', 'w')           # Cria o arquivo
# arq = open('teste.txt', 'a+')            # Abre o arq p/ leitura e escrita c/ o cursor no final
# # arq.write('Aula de AP 2')              # Escreve no arquivo
# # arq.write('BSI')
# # arq.write('Ana Caroline')
# #arq.close()                             # Fecha o arquivo
#
# # TESTAR A LEITURA DO ARQUIVO
# try:
#     arq = open('teste.txt', 'r')         # Abrir para leitura
# except: # else
#     arq = open('teste.txt', 'w')
#     arq.close()
#     arq = open('teste.txt', 'r')
#
# dados = arq.read()                       # Lê o arq texto inteiro e vai associar a variável do tipo string
# dados += 'Prof Carol muito querida <3'
# print(dados)
#
# print('--------------------------------------')
#
# arq.seek(0,0)                            # Volta o cursor para o inicio do arquivo
#
# # LER ATÉ O CARACTER DA POSIÇÃO 16
# trecho = arq.read(16)
# print(trecho)
#
# # LER ATÉ O CARACTER DA POSIÇÃO 17
# trecho = arq.read() # faz a partir de onde parou (16)
# print(trecho)
#
# arq.seek(0,0)
# lista = arq.readlines() # Adiciona na lista as linhas do arq de texto
# lista.append('Carol')
# lista.append('Bruno')
# print(lista)
#
# for linha in lista:
#     print(linha, end='')
#
# arq.close()
#
# # GRAVAR A LISTA NO ARQUIVO
# arq = open('teste.txt', 'w')
#
# for linha in lista:
#     arq.write(linha)
#
# arq.close()
import csv

# PARTE 2 - ARQUIVOS DE TEXTO DO TIPO CSV
arq_csv = open('arqAlunos.csv', 'w', newline='', encoding='utf-8')

campos = ['Nome', 'Idade']
gravar = csv.DictWriter(arq_csv, fieldnames = campos)
gravar.writeheader() # Gravar os campos na primeira linha
gravar.writerow({'Nome':'Ana', 'Idade':'18'})
gravar.writerow({'Nome':'Caroline', 'Idade':'25'})
arq_csv.close()
