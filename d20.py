import random

def dado_vinte():
    dado = list(range(1,21))
    numero_sorteado = random.choice(dado)
    return numero_sorteado

def menu():
    texto_topo = " D20 ".center(36,"=")
    texto_opcao = " [ENTER para rolar o dado] ".center(36)

    print(texto_topo)
    input(texto_opcao)
    return

def main():
    while True:
        menu()
        numero_sorteado = dado_vinte()
        resultado = f" Número sorteado:      {numero_sorteado}! ".center(36)
        linha_final = "".center(36,"=")



        print(resultado)

        if numero_sorteado == 20:
            acerto_critico = "Acerto crítico!".center(36)
            print(acerto_critico)
        elif numero_sorteado == 1:
            erro_critico = "Erro crítico!".center(36)
            print(erro_critico)
        
        print(linha_final)
        print("\n\n")

main()