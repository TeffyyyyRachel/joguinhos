def infos_basicas():
    titulo = " Informações Básicas ".center(36,"=")
    dados = {}

    print()
    print(titulo)

    dados["Nome"] = input("Nome do personagem: ")
    dados["Idade"] = input("Idade do personagem: ")
    dados["Gênero"] = input("Gênero do personagem: ")
    dados["Raça"] = input("Raça do personagem: ")
    dados["Classe"] = input("Classe/Profissão do personagem: ")

    return dados

def atributos_fis():
    atributos_fisicos = " Atributos Físicos ".center(36,"=")
    dados = {}

    print()
    print(atributos_fisicos)

    dados["Altura"] = input("Altura do personagem: ")
    dados["Peso"] = input("Peso do personagem: ")
    dados["Cor dos Olhos"] = input("Cor dos olhos do personagem: ")
    dados["Cor do Cabelo"] = input("Cor do cabelo do personagem: ")
    dados["Características Distintivas"] = input("Características distintivas (cicatrizes, tatuagens, etc.): ")

    return dados

def hab_atr():
    habilidades_atributos = " Habilidades e Atributos ".center(36,"=")
    dados = {}

    print()
    print(habilidades_atributos)
    
    dados["Força"] = input("Força do personagem (1-10): ")
    dados["Agilidade"] = input("Agilidade do personagem (1-10): ")
    dados["Inteligência"] = input("Inteligência do personagem (1-10): ")
    dados["Carisma"] = input("Carisma do personagem (1-10): ")
    dados["Sabedoria"] = input("Sabedoria do personagem (1-10): ")
    dados["Constituição"] = input("Constituição física do personagem (1-10): ")

    return dados

def equip():
    equipamentos = " Equipamentos ".center(36,"=")
    dados = {}
    
    print()
    print(equipamentos)

    dados["Arma Principal"] = input("Arma principal do personagem: ")
    dados["Armadura"] = input("Armadura do personagem: ")
    dados["Itens Mágicos"] = input("Itens mágicos do personagem: ")

    return dados

def hist_pers():
    historico_personalidade = " Histórico e Personalidade ".center(36,"=")
    dados = {}

    print()
    print(historico_personalidade)

    dados["História"] = input("História do personagem: ")
    dados["Motivação"] = input("Motivação do personagem: ")
    dados["Alinhamento"] = input("Alinhamento moral do personagem: ")
    dados["Medos"] = input("Medos ou fobias do personagem: ")
    dados["Objetivos"] = input("Objetivos ou aspirações do personagem: ")

    return dados

def relac():
    relacionamentos = " Relacionamentos ".center(36,"=")
    dados = {}
    
    print()
    print(relacionamentos)

    dados["Amigos/Companheiros"] = input("Amigos ou companheiros importantes do personagem: ")
    dados["Inimigos/Rivais"] = input("Inimigos ou rivais do personagem: ")
    dados["Família"] = input("Informações sobre a família do personagem: ")

    return dados

def criando_personagem():
    informacoes_basicas = infos_basicas()    
    atributos_fisicos = atributos_fis()
    habilidades_atributos = hab_atr()
    historico_personalidade = hist_pers()
    relacionamentos = relac()

    titulo_topo_final = " TODAS AS INFORMAÇÕES ".center(36,"=")

    print()
    print(titulo_topo_final)

    print("\n# Informações básicas")
    for key, value in informacoes_basicas.items():
        print(f"{key}: {value}")

    print("\n# Atributos físicos")
    for key, value in atributos_fisicos.items():
        print(f"{key}: {value}")

    print("\n# Habilidades e atributos")
    for key, value in habilidades_atributos.items():
        print(f"{key}: {value}")

    print("\n# Histórico e personalidade")
    for key, value in historico_personalidade.items():
        print(f"{key}: {value}")

    print("\n# Relacionamentos")
    for key, value in relacionamentos.items():
        print(f"{key}: {value}")

    print("\n!!! Salve essas informações em um bloco de notas para que não sejam perdidas. !!!")
    print()
    print("="*36)

criando_personagem()