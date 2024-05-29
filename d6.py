import random

def dado_seis():
    dado = list(range(1,7))
    numero_sorteado = random.choice(dado)
    return numero_sorteado

def menu():
    texto_topo = " D6 ".center(36,"=")
    texto_opcao = " [ENTER para rolar o dado] ".center(36)

    print(texto_topo)
    input(texto_opcao)
    return

def main():
    while True:
        menu()
        numero_sorteado = dado_seis()
        resultado = f" Número sorteado:      {numero_sorteado}! ".center(36)
        linha_final = "".center(36,"=")

        print(resultado)        
        print(linha_final)
        print("\n\n")

main()