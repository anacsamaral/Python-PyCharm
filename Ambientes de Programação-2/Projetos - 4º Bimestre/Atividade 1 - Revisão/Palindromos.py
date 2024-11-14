def verificar_palindromo(frase):
    frase_limpa = ''.join(frase.lower().split())
    return frase_limpa == frase_limpa[::-1]

frase_pessoa = input("Digite uma frase para verificar se é um palíndromo: ")

if verificar_palindromo(frase_pessoa):
    print(f'A frase "{frase_pessoa}" é um palíndromo!')
else:
    print(f'A frase "{frase_pessoa}" não é um palíndromo.')
