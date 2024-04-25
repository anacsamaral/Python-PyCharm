n1 = int(input('Digite o número 1: '))
n2 = int(input('Digite o número 2: '))
n3 = int(input('Digite o número 3: '))

if n1 > n2 and n1 > n3:
    print('O número %d é maior' %n1)
elif n2 > n1 and n2 > n3:
    print('O número %d é maior' %n2)
else:
    print('O número %d é maior' %n3)