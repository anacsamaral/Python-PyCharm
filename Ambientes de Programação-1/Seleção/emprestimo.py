sal = float(input('Digite o salário: '))
prest = float(input('Digite o valor da prestação: '))

if prest <= sal * (30 / 100):
    print('Você pode fazer um emprestimo!')
else:
    print('Você não pode fazer um empréstimo...')