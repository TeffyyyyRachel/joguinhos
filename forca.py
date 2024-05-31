import random

def sortear_palavra():
    palavras = [
    "python",
    "programacao",
    "computador",
    "algoritmo",
    "openai",
    "inteligencia",
    "artificial",
    "dados",
    "estrutura",
    "variavel",
    "funcao",
    "dicionario",
    "lista",
    "conjunto",
    "loop",
    "condicional",
    "arquivo",
    "texto",
    "numeros",
    "aleatorio"
]

    palavra_sorteada = random.choice(palavras)

    return palavra_sorteada

def situacao_jogo(letras_corretas, letras_erradas, palavra_sorteada, tentativas_restantes):
    print(f"Palavra secreta: {' '.join(letra if letra in letras_corretas else '_' for letra in palavra_sorteada)}")
    print(f"Letras corretas: {letras_corretas}")
    print(f"Letras erradas: {letras_erradas}")
    print(f"Tentativas restantes: {tentativas_restantes}")

def forca():
    texto_topo = " FORCA ".center(36,"=")
    instrucoes = "\n    Adivinhe a palavra sorteada\n          e vença o jogo!\n"

    print()
    print(texto_topo)
    print(instrucoes)

    palavra_sorteada = sortear_palavra()
    tentativas = 6
    palavra_sorteada_censurada = " ".join(["_"]*len(palavra_sorteada))
    letras_corretas = []
    letras_erradas = []

    print(f" A palavra sorteada é esta: {palavra_sorteada_censurada}\n")

    while True:
        
        if len(letras_corretas) == len(set(palavra_sorteada)):
            print("\n!!! VOCÊ GANHOU !!!\n")
            break

        suposicao_jogador = input("\n    Escolha uma letra: ").lower()
        
        if len(suposicao_jogador) != 1 or not suposicao_jogador.isalpha():
            print("\n!!! Insira apenas uma letra. !!!\n")
            continue

        
        if suposicao_jogador in letras_corretas or suposicao_jogador in letras_erradas:
            print("\nEsta letra já foi inserida.\n")
            continue

        if suposicao_jogador in palavra_sorteada:
            print("\nLetra EXISTE na palavra secreta!\n")
            letras_corretas.append(suposicao_jogador)

        if suposicao_jogador not in palavra_sorteada:
            print("\nLetra não existe na palavra...\n")
            letras_erradas.append(suposicao_jogador)
            tentativas -= 1

        conjunto_letras_corretas = ", ".join(letras_corretas)
        conjunto_letras_erradas = ", ".join(letras_erradas)
        situacao_jogo(conjunto_letras_corretas, conjunto_letras_erradas, palavra_sorteada, tentativas)

        if tentativas == 0:
            print("\nVocê perdeu...\n")
            break

forca()