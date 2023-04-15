import json
import os
import random

local_perguntas = 'data/perguntas.json'
local_resposta = 'data/respostas.json'
local_identificacao = 'data/usuarios'

# abre o arquivo JSON
with open('usuarios.json', 'r', encoding="UTF-8") as arquivo:
    usuarios = json.load(arquivo)

for usuario in usuarios:
    if usuario["id_usuario"] == '0/0':
        nome = usuario['identificacao']

# exibe o nome escolhido
print("Olá, {}!\nSeja muito bem vindo ao nosso Sistema de Avaliação 360º! O que deseja fazer?".format(nome))


y = True
while y:
    entrada_avaliacao = input("\n1 - Responder Avaliação"
                              "\n"
                              "\n2 - Sair"
                              "\n"
                              "\n"
                              "Escolha uma opção: ")

    if entrada_avaliacao == '1':
        print("\nOpção 1 selecionada: 'Responder avaliação'")

        # Verifica se o arquivo JSON já existe
        if os.path.exists(local_perguntas):
            # Se existir, carrega as perguntas existentes
            with open(local_perguntas, 'r', encoding="UTF-8") as arquivo:
                perguntas = json.load(arquivo)
        else:
            # Se não existir, cria uma lista vazia
            perguntas = []

        # Lista para armazenar as respostas
        respostas = []

        # Função para obter a resposta do usuário como um número inteiro entre 1 e 5
        def obter_resposta():
            while True:
                try:
                    resposta = int(input("\nPor favor, avalie de 1 a 5: "))
                    if resposta < 1 or resposta > 5:
                        raise ValueError
                    break
                except ValueError:
                    print(
                        "\nNúmero Invalido\nPor favor, insira um número inteiro entre 1 e 5.")
            return resposta

        # Loop para obter as respostas do participante
        for pergunta in perguntas:
            print(pergunta["descricao"])
            resposta = {'ip': str(pergunta["ip"]),
                        'resp': str(obter_resposta())}
            respostas.append(resposta)

        # Salvar as respostas em um arquivo JSON
        with open(local_resposta, "w") as arquivo:
            json.dump(respostas, arquivo, indent=5)

        print("\nRespostas salvas em respostas_avaliacao.json.\n")
        y = False

    elif entrada_avaliacao == '2':
        print("\nOpção 2 selecionada: 'Sair'\n\nSaindo...\n")
        y = False
    else:
        print("\nOpção inválida.\nPor favor, escolha uma opção válida.\n")

print("Fim da Avaliação, agradeçemos a sua participação.\n")
