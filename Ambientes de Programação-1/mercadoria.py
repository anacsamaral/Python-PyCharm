preco = float(input('Preço da mercadoria: '))
desconto = int(input('Porcentagem de desconto: '))

desconto = float(preco * (desconto/100))
valor_final = float(preco - desconto)

print('Desconto de R$ %.2f em uma mercadoria de R$ %.2f' % (desconto, preco))
print('Valor do desconto: R$ %.2f' % desconto)
print('Valor a pagar: R$ %.2f' % valor_final)