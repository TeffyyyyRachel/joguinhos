import random

def jogada_pc():
	jogadas = ["Pedra", "Papel", "Tesoura"]
	pc_jogou = random.choice(jogadas)
	return pc_jogou

def verificar_vitoria(jogada_humana, jogada_maquina):
	
	if jogada_humana == jogada_maquina:
		return "\n\t\t\t\t         Empate!\n"
		
	elif (jogada_humana == "Pedra" and jogada_maquina == "Tesoura") or (jogada_humana == "Papel" and jogada_maquina == "Pedra") or (jogada_humana == "Tesoura" and jogada_maquina == "Papel"):
		return "\n\t\t\t\t   Vitória do jogador! \n"
		
	elif (jogada_maquina == "Pedra" and jogada_humana == "Tesoura") or (jogada_maquina == "Papel" and jogada_humana == "Pedra") or (jogada_maquina == "Tesoura" and jogada_humana == "Papel"):
		return "\n\t\t\t\t  Vitória do computador! \n"
		
	else:
		return "\n\t\t\t\t   Ninguém venceu... \n"

def menu():
	print("\t  === JOKENPO! ===")
	print("\n\t     1 - Pedra")
	print("\t     2 - Papel")
	print("\t     3 - Tesoura")
	print("\n\t  " + "="*16)
	jogada = input("\n\tQUAL SERÁ A SUA JOGADA? ")
	
	if jogada == "1":
		return "Pedra"
	elif jogada == "2":
		return "Papel"
	elif jogada == "3":
		return "Tesoura"
	else:
		return "Jogada invalida. Apenas nums de 1 a 3."

def main():
	pontuacao_jogador = 0
	pontuacao_pc = 0
	
	while True:
		jogada_humana = menu()
		jogada_maquina = jogada_pc()
		
		aviso_vitoria = ""
		
		narracao_jogador = "\n\t\t\t\t Jogador:\t"
		narracao_pc = "\t\t\t\t Computador:\t"
		
		print("\n\t\t\t\t     === JOGADAS ===")
		print(narracao_jogador, jogada_humana)
		print(narracao_pc, jogada_maquina)
		
		aviso_vitoria = verificar_vitoria(jogada_humana, jogada_maquina)
		
		if aviso_vitoria == "\n\t\t\t\t   Vitória do jogador! \n":
			pontuacao_jogador += 1
		elif aviso_vitoria == "\n\t\t\t\t  Vitória do computador! \n":
			pontuacao_pc += 1
		
		print(aviso_vitoria)
		print(f"\t\t\t\t  > Jogador {pontuacao_jogador} X PC {pontuacao_pc} <\n")
	
	
main()