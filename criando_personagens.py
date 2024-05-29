class Personagem:
    def __init__(self, nome, idade, classe, raca, alinhamento):
        self.nome = nome
        self.idade = idade
        self.classe = classe
        self.raca = raca
        self.alinhamento = alinhamento

    def atacar(self):
        if self.classe == "Guerreiro":
            print(f"{self.nome} ataca com arma pesada!")
        elif self.classe == "Mago":
            print(f"{self.nome} ataca com magia!")
        elif self.classe == "Ladino":
            print(f"{self.nome} ataca sorrateiramente...")
        elif self.classe == "Arqueiro":
            print(f"{self.nome} atira flechas!")
        else:
            print(f"{self.nome} ataca!")
    
    def descansar(self):
        print(f"{self.nome} está descansando...")
    
personagem_1 = Personagem("Lian", 26, "Ladino", "Humano", "Neutral-Good")
personagem_1.atacar()
personagem_1.descansar()

print()

personagem_2 = Personagem("Salin", 19, "Mago", "Elfo", "Lawful-Good")
personagem_2.atacar()
personagem_2.descansar()