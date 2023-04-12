import json
import os

local_perguntas = 'data/perguntas.json'
local_resposta = 'data/respostas.json'

y = True
while y:
    entrada_avaliacao = input("\n1-Responder Avaliação"
                            "\n"
                            "\n2-Sair"
                            "\n"
                            "\n"
                            "Escolha sua opção: ")

    if entrada_avaliacao == '1':
        print("\nOpção 1 selecionada: Responder avaliação.\n")

    # Definindo as perguntas como uma lista de dicionários

    # Verifica se o arquivo JSON já existe
        if os.path.exists(local_perguntas):
            # Se existir, carrega os usuários existentes
            with open(local_perguntas, 'r') as arquivo:
                perguntas = json.load(arquivo)
        else:
            # Se não existir, cria uma lista vazia
            perguntas = []

        # Função para obter a resposta do usuário como um número inteiro entre 1 e 5
        def obter_resposta():
            while True:
                try:
                    resposta = int(input("\nPor favor, avalie de 1 a 5: \n"))
                    if resposta < 1 or resposta > 5:
                        raise ValueError
                    break
                except ValueError:
                    print("\nPor favor, insira um número inteiro entre 1 e 5.")
            return resposta

        # Loop para obter as respostas do participante
        x = 1
        for pergunta in perguntas:
            print(pergunta["descricao"])
            resposta = {'ip': str(x),
                        'resp': str(obter_resposta())}
            x = x + 1
            if os.path.exists(local_resposta):
                # Se existir, carrega os usuários existentes
                with open(local_resposta, 'r') as arquivo:
                    respostas = json.load(arquivo)
            else:
                # Se não existir, cria uma lista vazia
                respostas = []
            respostas.append(resposta)

        # Salvar as respostas em um arquivo JSON
        with open(local_resposta, "w") as arquivo:
            json.dump(respostas, arquivo, indent=5)

        print("\nRespostas salvas em respostas_avaliacao.json.\n")
        y = False

    elif entrada_avaliacao == '2':
        print("\nOpção 2 selecionada.\n\nSaindo...\n")
        y = False
    else:
        print("\nOpção inválida.\nPor favor, escolha uma opção válida.\n")