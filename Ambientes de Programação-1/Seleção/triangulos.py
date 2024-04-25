l1 = int(input('Digite a medida do lado 1: '))
l2 = int(input('Digite a medida do lado 2: '))
l3 = int(input('Digite a medida do lado 3: '))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    if l1 == l2 and l1 == l3:
        print('Este triângulo possui os 3 lados iguais. Portanto, é um triângulo equilátero!!!')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Este triângulo possui 2 lados iguais. Portando, é um triângulo isósceles!!!')
    else:
        print('Este triângulo possui todos os lados diferentes. Portanto, é um triângulo escaleno!!!')
else:
    print('Essas medidas não formam um triângulo:(')