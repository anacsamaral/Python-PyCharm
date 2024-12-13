def arvore_decisao():
    print("Bem-vindo à Árvore de Decisão da Saúde!")

    # Primeira pergunta
    resposta = input("Qual o ST_Slope? (UP, DOWN OU FLAT): ")

    if resposta == "UP":
        resposta = input(
            "Qual o tipo de dor no peito? (ATA, NAP, AT ou ASY): ")
        if resposta == 'ATA' or resposta == 'NAP' or resposta == 'AT':
            resposta = int(input("Qual o valor do pico antigo?: "))
            if resposta > 2:
                print("0% de Chance de Doença Cardíaca.")
            else:
                resposta = int(input("Qual a idade? : "))
                if resposta <= 56:
                    print("98% de Chance de Doença Cardíaca.")
                else:
                    resposta = int(input("Qual o colesterol sérico? : "))
                    if resposta <= 0:
                        resposta = int(input("Qual a PA em repouso? : "))
                        if resposta > 138:
                            print("0% de Chance de Doença Cardíaca.")
                        else:
                            resposta = int(input("Qual a idade? : "))
                            if resposta > 62:
                                print("100% de Chance de Doença Cardíaca.")
                            else:
                                print("50% de Chance de Doença Cardíaca.")
                    else:
                        resposta = int(input("Qual a idade? : "))
                        if resposta > 59:
                            print("96% de Chance de Doença Cardíaca.")
                        else:
                            resposta = input("Qual o tipo de dor no peito? (ATA, NAP ou AT): ")
                            if resposta == "ATA" or resposta == "AT" :
                                resposta = int(input("Qual a PA em repouso? : "))
                                if resposta > 150:
                                    print("0% de Chance de Doença Cardíaca.")
                                else:
                                    print("66% de Chance de Doença Cardíaca.")
                            else:
                                print("100% de Chance de Doença Cardíaca")
        else:
            resposta = float(input("Qual o valor do pico antigo?: "))
            if resposta <= 0.4:
                resposta = int(input("Qual o colesterol sérico?: "))
                if resposta <= 0:
                    resposta = int(input("Qual o jejum BS?: "))
                    if resposta == 1:
                        print("0% de Chance de Doença Cardíaca")
                    else:
                        resposta = int(input("Qual a idade? : "))
                        if resposta > 60:
                            print("0% de Chance de Doença Cardíaca.")
                        else:
                            resposta = int(input("Qual a PA em repouso? : "))
                            if resposta > 120:
                                print("100% de Chance de Doença Cardíaca.")
                            else:
                                print("33% de Chance de Doença Cardíaca.")
                else:
                    resposta = int(input("Qual a FC máxima? : "))
                    if resposta <= 148:
                        print("97,3% de Chance de Doença Cardíaca.")
                    else:
                        resposta = input("Qual a ECG em repouso? (NORMAL / ST / HVE: ")
                        if resposta == 'NORMAL' or resposta == 'ST':
                            resposta = int(input("Qual o colesterol sérico?"))
                            if resposta > 255:
                                print("100% de Chance de Doença Cardíaca.")
                            else:
                                resposta = int(input("Qual a FC máxima?: "))
                                if resposta <= 155:
                                    print("100% de Chance de Doença Cardíaca.")
                                else:
                                    resposta = int(input("Qual a idade: "))
                                    if resposta > 40:
                                        print("100% de Chance de Doença Cardíaca.")
                                    else:
                                        print("50% de Chance de Doença Cardíaca.")
                        else:
                            resposta = input("Qual o sexo? (M / F)")
                            if resposta == 'M':
                                print("0% de Chance de Doença Cardíaca.")
                            else:
                                resposta = int(input("Idade: "))
                                if resposta > 40:
                                    print("100% de Chance de Doença Cardíaca.")
                                else:
                                    print("50% de Chance de Doença Cardíaca.")
            else:
                resposta = int(input("Qual o colesterol sérico?"))
                if resposta > 349:
                    print("100% de Chance de Doença Cardíaca.")
                else:
                    resposta = input("Teve a angina durante exercicio? (S/N): ")
                    if resposta == 'S':
                        resposta = int(input("Qual o Jejum BS?: "))
                        if resposta == 1:
                            print("0% de Chance de Doença Cardíaca.")
                        else:
                            print("50% de Chance de Doença Cardíaca.")
                    else:
                        resposta = int(input("PA em repouso?: "))
                        if resposta > 125:
                            print("100% de Chance de Doença Cardíaca.")
                        else:
                            print("0% de Chance de Doença Cardíaca.")
    else:
        resposta = input(
            "Qual o tipo de dor no peito? (ATA, NAP, AT ou ASY): ")
        if resposta == "ATA" or resposta == "NAP" or resposta == "AT":
            resposta = int(input("Qual a FC máxima?: "))
            if resposta <= 136:
                resposta = input("Teve angina durante exercicio (S/N)?: ")
                if resposta == 'N':
                    resposta = input("Qual o sexo? (F/M): ")
                    if resposta == 'F':
                        resposta = int(input("Qual o colesterol?: "))
                        if resposta > 226:
                            print("50% de Chance de Doença Cardíaca.")
                        else:
                            print("100% de Chance de Doença Cardíaca.")
                    else:
                        resposta = int(input("Qual o colesterol? : "))
                        if resposta > 234:
                            print("0% de Chance de Doença Cardíaca.")
                        else:
                            resposta = int(input("Qual o jejum BS: "))
                            if resposta == 1:
                                resposta = int(input("Qual a idade?: "))
                                if resposta > 68:
                                    print("50% de Chance de Doença Cardíaca.")
                                else:
                                    print("0% de Chance de Doença Cardíaca.")
                            else:
                                resposta = int(input("Qual a PA em repouso?: "))
                                if resposta <= 105:
                                    print("0% de Chance de Doença Cardíaca.")
                                else:
                                    resposta = int(input("Qual o pico antigo?: "))
                                    if resposta > 0:
                                        print("100% de Chance de Doença Cardíaca.")
                                    else:
                                        print("66% de Chance de Doença Cardíaca.")
                else:
                    resposta = int(input("PA em repouso? : "))
                    if resposta > 130:
                        print("0% de Chance de Doença Cardíaca.")
                    else:
                        resposta = int(input("Qual o colesterol?: "))
                        if resposta <= 0:
                            print("0% de Chance de Doença Cardíaca.")
                        else:
                            resposta = int(input("Pico antigo?: "))
                            if resposta > 0:
                                print("50% de Chance de Doença Cardíaca.")
                            else:
                                print("0% de Chance de Doença Cardíaca.")
            else:
                resposta = input("Qual o sexo? F / M : ")
                if resposta == 'F':
                    resposta = int(input("Qual o pico antigo?: "))
                    if resposta > 1:
                        print("100% de Chance de Doença Cardíaca.")
                    else:
                        resposta = int(input("Idade?: "))
                        if resposta <= 45:
                            print("100% de Chance de Doença Cardíaca.")
                        else:
                            resposta = int(input("Qual a FC maxima?: "))
                            if resposta <= 150:
                                print("0% de Chance de Doença Cardíaca.")
                            else:
                                resposta = int(input("Qual o colesterol?: "))
                                if resposta > 248:
                                    print("100% de Chance de Doença Cardíaca.")
                                else:
                                    print("25% de Chance de Doença Cardíaca.")
                else:
                    resposta = int(input("Qual o ST_Slope (DOWN/FLAT)? : "))
                    if resposta == 'DOWN':
                        resposta = int(input("Qual o tipo de dor no peito? (ATA, NAP, AT): "))
                        if resposta == 'ATA':
                            print("50% de Chance de Doença Cardíaca.")
                        else:
                            print("100% de Chance de Doença Cardíaca.")
                    else:
                        resposta = int(input("Qual o colesterol? : "))
                        if resposta > 245:
                            print("100% de Chance de Doença Cardíaca.")
                        else:
                            resposta = int(input("Qual o tipo de dor no peito? (ATA, NAP ou TA): "))
                            if resposta == "ATA":
                                print("100% de Chance de Doença Cardíaca.")
                            else:
                                resposta = int(input("Qual o colesterol? : "))
                                if resposta > 237:
                                    print("100% de Chance de Doença Cardíaca.")
                                else:
                                    resposta = int(input("Qual a idade?: "))
                                    if resposta > 61:
                                        resposta = int(input("Qual a PA em repouso? : "))
                                        if resposta > 130:
                                            print("50% de Chance de Doença Cardíaca.")
                                        else:
                                            print("50% de Chance de Doença Cardíaca.")
                                    else:
                                        resposta = int(input("Qual o colesterol?: "))
                                        if resposta > 228:
                                            print("0% de Chance de Doença Cardíaca.")
                                        else:
                                            resposta = int(input("Qual a ECG em repouso? (NORMAL, ST ou HVE): "))
                                            if resposta == 'NORMAL':
                                                print("0% de Chance de Doença Cardíaca.")
                                            else:
                                                resposta = int(input("Qual a PA em repouso? : "))
                                                if resposta > 120:
                                                    print("50% de Chance de Doença Cardíaca.")
                                                else:
                                                    print("100% de Chance de Doença Cardíaca.")
        else:
            resposta = input("Qual o sexo (F / M?: ")
            if resposta == 'F':
                resposta = int(input("Qual o Jejum BS?: "))
                if resposta == 1:
                        print("0% de Chance de Doença Cardíaca")
                else:
                    resposta = float(input("Qual o pico antigo? : "))
                    if resposta > 1.6:
                        resposta = int(input("Qual a idade? : "))
                        if resposta > 62:
                            print("33% de Chance de Doença Cardíaca.")
                        else:
                            print("0% de Chance de Doença Cardíaca.")
                    else:
                        resposta = input("Qual o ECG em repouso?(NORMAL, HVE ou ST): ")
                        if resposta == 'NORMAL':
                            resposta = int(input("Qual a FC maxima?: "))
                            if resposta > 140:
                                print("0% de Chance de Doença Cardíaca.")
                            else:
                                resposta = int(input("Qual a PA em repouso?: "))
                                if resposta > 130:
                                    print("50% de Chance de Doença Cardíaca.")
                                else:
                                    print("100% de Chance de Doença Cardíaca.")
                        else:
                            resposta = int(input("Qual o PA em repouso?: "))
                            if resposta > 140:
                                print("33% de Chance de Doença Cardíaca.")
                            else:
                                print("100% de Chance de Doença Cardíaca.")
            else:
                resposta = int(input("Qual o pico antigo?"))
                if resposta <= 0.1:
                    print("0% de Chance de Doença Cardíaca.")
                else:
                    resposta = float(input("Qual o pico antigo?"))
                    if resposta <= 0.5:
                        resposta = int(input("Qual o colesterol?"))
                        if resposta <= 186:
                            print("0% de Chance de Doença Cardíaca.")
                        else:
                            resposta = int(input("Qual a FC maxima?"))
                            if resposta > 161:
                                print("0% de Chance de Doença Cardíaca.")
                            else:
                                print("100% de Chance de Doença Cardíaca.")
                    else:
                        resposta = int(input("Qual a PA em repouso?"))
                        if resposta > 126:
                            print("3,1% de Chance de Doença Cardíaca.")
                        else:
                            resposta = int(input("Qual o Jejum BS?"))
                            if resposta == 1:
                                print("0% de Chance de Doença Cardíaca.")
                            else:
                                resposta = input("Qual o ECG em repouso (NORMAL, ST ou HVE)?")
                                if resposta == 'ST':
                                    resposta = int(input("Qual o colesterol?"))
                                    if resposta > 260:
                                        print("0% de Chance de Doença Cardíaca.")
                                    else:
                                        print("75% de Chance de Doença Cardíaca.")
                                else:
                                    resposta = int(input("Qual a frequencia maxima?"))
                                    if resposta <= 125:
                                        print("0% de Chance de Doença Cardíaca.")
                                    else:
                                        resposta = int(input("Qual a idade?"))
                                        if resposta <= 39:
                                            print("0% de Chance de Doença Cardíaca.")
                                        else:
                                            resposta = float(input("Qual o pico antigo?"))
                                            if resposta <= 1.5:
                                                print("100% de Chance de Doença Cardíaca.")
                                            else:
                                                resposta = int(input("Qual a PA em repouso?"))
                                                if resposta > 104:
                                                    print("0% de Chance de Doença Cardíaca.")
                                                else:
                                                    print("100% de Chance de Doença Cardíaca.")
# Executar a árvore de decisão
arvore_decisao()
