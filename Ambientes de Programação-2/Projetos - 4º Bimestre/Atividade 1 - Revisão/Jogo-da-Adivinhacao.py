from random import randint

def sortear_numero():
    return randint(0, 100)

def obter_chute(tentativa, max_tentativas):
    while True:
        try:
            chute = int(input(f"Tentativa {tentativa}/{max_tentativas}: Digite seu chute: "))
            return chute
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

def jogar():
    numero_sorteado = sortear_numero()
    tentativas = 0
    max_tentativas = 20

    print("Bem-vindo ao Jogo da Adivinhação!")
    print("Tente adivinhar o número sorteado entre 0 e 100.")

    while tentativas < max_tentativas:
        tentativas += 1
        chute = obter_chute(tentativas, max_tentativas)

        if chute == numero_sorteado:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativa(s).")
            break
        elif chute < numero_sorteado:
            print("O número sorteado é maior.")
        else:
            print("O número sorteado é menor.")

    if tentativas == max_tentativas and chute != numero_sorteado:
        print(f"Você não conseguiu acertar o número em {max_tentativas} tentativas. O número era {numero_sorteado}.")

def start():
    while True:
        jogar()
        jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            print("Obrigado por jogar! Até a próxima.")
            break

start()
