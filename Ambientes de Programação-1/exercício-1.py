preco = float(input('Preço da mercadoria: '))
percent = float(input('Percentual de desconto: '))

descont = float(preco * (percent/100))
valorF = float(preco - descont)

print('Desconto de {:.2f} em uma mercadoria de {:.2f}' .format(descont, preco))
print('Desconto: %.2f', %descont)
print('Valor a pagar: %.2f', %valorF)