import random

def vencedor(jogador, computador):
    if jogador == computador:
        return "Empate!"

    if (jogador == "pedra" and computador == "tesoura") or \
            (jogador == "tesoura" and computador == "papel") or \
            (jogador == "papel" and computador == "pedra"):
        return "Você ganhou!"

    return "Computador ganhou!"

def jogar():
    opcoes = ["pedra", "papel", "tesoura"]

    print("Bem-vindo ao Pedra, Papel, Tesoura!")

    jogador = input("Escolha 'pedra', 'papel' ou 'tesoura': ").lower()

    if jogador not in opcoes:
        print("Escolha inválida! Tente novamente.")
        return

    computador = random.choice(opcoes)

    print(f"Você escolheu: {jogador}")
    print(f"Computador escolheu: {computador}")

    resultado = vencedor(jogador, computador)
    print(resultado)

def iniciar():
    while True:
        jogar()
        jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            print("Fim de Jogo!")
            break

iniciar()