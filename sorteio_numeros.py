import random

def sortear_numeros(numero_inicial, numero_final):
    lista_numeros = range(numero_inicial,numero_final+1)
    numero_sorteado = random.choice(lista_numeros)

    return numero_sorteado

def escolha_numeros():
    titulo_inicio = " SORTEADOR DE NÚMEROS ".center(36,"=")
    instrucoes = "\n    Escolha dois números, com o \n    primeiro obrigatoriamente \n    MENOR do que o segundo,\n    e um número será sorteado \n    entre esses dois.\n"
    numero_inicial = 0
    numero_final = 0

    print(titulo_inicio)
    print(instrucoes)

    while True:
        try:
            numero_inicial = int(input("    Primeiro número: "))
            numero_final = int(input("    Último número: "))
            if numero_inicial >= numero_final:
                print("\n!!! O primeiro número deve ser MENOR que o segundo. !!!\n")
                continue
            break
        except ValueError:
            print("\n!!! Por favor, envie apenas números em ambos os campos. !!!\n")

    while True:
        numero_sorteado = sortear_numeros(numero_inicial, numero_final)
        print(f"\n=== O número sorteado entre {numero_inicial} e {numero_final} foi {numero_sorteado}! ===\n")
        escolha = input(f" [ENTER] para sortear de novo entre {numero_inicial} e {numero_final} ou 'sair' para encerrar. ").lower()
        if escolha == "sair":
            break

escolha_numeros()