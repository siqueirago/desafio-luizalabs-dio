# Exercício 06 - Palíndromos 


def verificar_palindromo():
	palavra = input("Digite uma palavra: ").lower()
	if palavra == palavra[::-1]:
		print("A palavra é um palíndromo")
	else:
		print("A palavra não é um palíndromo")
