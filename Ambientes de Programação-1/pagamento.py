preco = float(input('Digite o preço: '))

print(' 1 - À vista em dinheiro ou cheque, recebe 10% de desconto\n 2 - À vista no cartão de crédito, recebe 5% de desconto\n 3 - Em 2 vezes, preço normal de venda sem juros\n 4 - Em 3 vezes, preço normal de venda mais juros de 10%\n')

cod = int(input('Escolha a condição de pagamento: '))

if cod == 1:
    valorF = float(preco - (preco * 0.10))
    print('Valor a ser pago: R$%.2f' % valorF)
elif cod == 2:
    valorF = float(preco - (preco * 0.05))
    print('Valor a ser pago: R$%.2f' % valorF)
elif cod == 3:
    valorF = preco
    print('Valor a ser pago: R$%.2f' % valorF)
else:
    valorF = float(preco + (preco * 0.10))
    print('Valor a ser pago: R$%.2f' % valorF)