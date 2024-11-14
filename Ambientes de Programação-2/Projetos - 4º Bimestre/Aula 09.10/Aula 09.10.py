# print('''O curso de Agronegócio tem como objetivo a formação sólida e aprofundada na criação e gestão das organizações do agronegócio em seus vários aspectos e inter-relações, atendendo necessidades de adaptação às transformações ambientais, tecnológicas e gerenciais.
#
# Durante o curso de Agronegócio, você estará em contato com disciplinas como Produção Animal e Vegetal, Logística, Marketing e Legislação. Bem como Mercado do Agronegócio, Cadeias Produtivas, Gestão Ambiental, Administração Financeira, entre outras.
#
# Pela sua vasta diversidade ambiental, o Brasil se destaca no cenário da agricultura e da pecuária no mundo. Desta forma, o mercado de trabalho para este tecnólogo em Agronegócio é amplo e cada vez mais procurado. A economia do setor cresceu muito nos últimos anos, aumentando as oportunidades de emprego em pequenas e grandes propriedades rurais.''')
#
# nome = input('Informe seu Nome: ')
# print('Seu nome é:', nome)
#
# idade = int(input('Informe sua Idade:'))
# print('Sua idade é:', idade)
#
# altura = float(input('Informe sua Altura (m):'))
# print('Sua altura é:', altura)
#
# print('Seu nome é', nome, 'Você tem', idade, 'anos de idade e mede', altura, 'de altura!!!')
# print('Seu nome é %s, você tem %d anos de idade e mede %.2f de altura!!!' %(nome, idade, altura))
#
# print('Seu nome é {}, você tem {} anos de idade e mede {} de altura!!!'.format(nome, idade, altura))

#PEDAÇOS DE STRING
frase = 'Adoro programar em Python'
print(frase[::-1])  # Inverter
print(frase[:5])

nome1 = 'Zezinho'
nome2 = 'Jose' #se colocar minusculo, jose sera maior, pois de acordo com a tabela ascii, o j minusculo vem depois do Z maiusculo

if nome1 > nome2:
    print(nome1, 'é maior que', nome2)
else:
    print(nome2, 'é maior que', nome1)

