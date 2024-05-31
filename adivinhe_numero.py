import random

def sortear_numero(numero_inicial, numero_final):
    conjunto_numeros = range(numero_inicial,numero_final+1)
    numero_sorteado = random.choice(conjunto_numeros)

    return numero_sorteado

def escolher_numero():
    titulo_topo = " ADIVINHE O NÚMERO ".center(36,"=")
    instrucoes = "\n    Escolha dois números e \n    o computador irá sortear um\n    número do intervalo entre eles.\n    Você terá que adivinhar\n    qual o número foi sorteado!\n"
    numero_inicial = 0
    numero_final = 0

    print(titulo_topo)
    print(instrucoes)

    while True:
        try:
            numero_inicial = int(input("    Primeiro número: "))
            numero_final = int(input("    Segundo número: "))
            if numero_inicial >= numero_final:
                print("\n!!! O primeiro número dever ser MENOR do que o segundo. !!!\n")
                continue
            break
        except ValueError:
            print("!!! Insira apenas números inteiros em ambos os campos. !!!\n")
    
    numero_sorteado = sortear_numero(numero_inicial,numero_final)
    print("\n    Número sorteado com sucesso!\n")

    while True:
        try:
            suposicao_jogador = int(input("Qual a sua suposição? "))
            if suposicao_jogador == numero_sorteado:
                print("\nVocê acertou, parabéns!\n")
                break
            elif suposicao_jogador > numero_sorteado:
                print("\nSeu chute foi mais ALTO do que a resposta...\n")
            elif suposicao_jogador < numero_sorteado:
                print("\nSeu chute foi mais BAIXO do que a resposta...\n")
        except ValueError:
            print("!!! Insira apenas números inteiros em ambos os campos. !!!\n")

    
escolher_numero()