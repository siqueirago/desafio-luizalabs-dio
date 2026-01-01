# Menu Interativo - Resolvendo Códigos em Python com Copiloto de IA

# Importando as funções dos exercícios
from codigo.exercicios.ex01_concatenar_dados import concatenar_dados
from codigo.exercicios.ex02_repetindo_textos import repetir_texto
from codigo.exercicios.ex03_operacoes_matematica import operacoes_matematicas
from codigo.exercicios.ex04_par_ou_impar import verificar_paridade
from codigo.exercicios.ex05_calcular_media import calcular_media
from codigo.exercicios.ex06_palindromos import verificar_palindromo



def exibir_menu():
	print("\n=== MENU PRINCIPAL ===")
	print("1 - Concatenar dados")
	print("2 - Repetir textos")
	print("3 - Operações matemáticas")
	print("4 - Par ou ímpar")
	print("5 - Média de notas")
	print("6 - Verificar palíndromo")
	print("0 - Sair")

def executar():
	while True:
		exibir_menu()
		try:
			opcao = int(input("Escolha uma opção: "))
		except ValueError:
			print("Opção inválida. Digite um número.")
			continue

		if opcao == 1:
			concatenar_dados()
		elif opcao == 2:
			repetir_texto()
		elif opcao == 3:
			operacoes_matematicas()
		elif opcao == 4:
			verificar_paridade()
		elif opcao == 5:
			calcular_media()
		elif opcao == 6:
			verificar_palindromo()
		elif opcao == 0:
			print("Encerrando o programa...")
			break
		else:
			print("Opção inexistente. Tente novamente.")

if __name__ == "__main__":
	executar()