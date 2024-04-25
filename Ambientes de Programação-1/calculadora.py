n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

cod = int(input('Escolha a operação desejada:\n 1) Adição\n 2) Subtração\n 3) Multiplicação\n 4) Divisão\n 5) Raiz Quadrada\n 6) Potência\n'))

if cod == 1:
    soma = n1 + n2
    print('A soma de %d e %d é: %d' %(n1, n2, soma))
elif cod == 2:
    sub = n1 - n2
    print('A subtração de %d e %d é: %d' %(n1, n2, sub))
elif cod == 3:
    mult = n1 * n2
    print('A multiplicação de %d por %d é: %d' %(n1, n2, mult))
elif cod == 4:
    divs = n1 / n2
    print('A divisão de %d por %d é: %.2f' %(n1, n2, divs))
elif cod == 5:
    raiz1 = (n1 ** (1/2))
    raiz2 = (n2 ** (1/2))
    print('A raiz de %d é: %.2f. A raiz de %d é %.2f' %(n1, raiz1, n2, raiz2))
else:
    pot = n1 ** n2
    print('%d elevado a %d é: %d' %(n1, n2, pot))
