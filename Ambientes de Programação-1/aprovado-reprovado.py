num = int(input('Digite 1 para iniciar ou 0 para sair: '))

while num > 0:
    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))
    freq = int(input('Digite a porcentagem da frequência: '))
    media = (nota1 + nota2) / 2
    print('Sua média é: %.2f' % media)
    if media >= 6.0 and freq >= 75:
        print('Aprovado em nota e frequência, parabéns!')
    elif media >= 6.0 and freq < 75:
        print('Aprovado apenas em nota\n Reprovado em frequência')
    elif media < 6.0 and freq >= 75:
        print('Aprovado apenas em frequência\n Reprovado em nota')
    else:
        print('Reprovado em nota e frequência :(')

    num = int(input('Digite 1 para iniciar ou 0 para sair: '))

print('Fim do programa!\n')