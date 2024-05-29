import random

def moeda():
    moeda = ["Cara", "Coroa"]
    lado_sorteado = random.choice(moeda)
    return lado_sorteado

def menu():
    texto_topo = "".center(36,"=")
    texto_opcao = " [ENTER para jogar a moeda] ".center(36)

    print(texto_topo)
    input(texto_opcao)
    return

def main():
    while True:
        menu()
        lado_sorteado = moeda()
        resultado = f" Resultado:        {lado_sorteado}! ".center(36)
        linha_final = "".center(36,"=")

        print(resultado)
        print(linha_final)
        print("\n\n")

main()