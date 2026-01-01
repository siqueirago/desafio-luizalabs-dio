# Exercício 01 - Concatenando Dados


def concatenar_dados():
    nome = input("Digite seu nome: ")
    sobrenome = input("Digite seu sobrenome: ")
    idade = input("Digite sua idade: ")
    dados_concatenados = f"Nome: {nome} {sobrenome}, Idade: {idade}"
    print(dados_concatenados)