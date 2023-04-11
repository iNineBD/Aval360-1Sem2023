import json
import os

entrada_avaliacao = input("1-Responder Avaliação"
                          "\n"
                          "2-Sair"
                          "\n"
                          "\n"
                          "Escolha sua opção: ")

if entrada_avaliacao == '1':
    print("Opção 1 selecionada. Responder avaliação.")

    # Função para obter a resposta do usuário como um número inteiro entre 1 e 5
    def obter_resposta():
        while True:
            try:
                resposta = int(input("Por favor, avalie de 1 a 5: "))
                if resposta < 1 or resposta > 5:
                    raise ValueError
                break
            except ValueError:
                print("Por favor, insira um número inteiro entre 1 e 5.")
        return resposta

    # Definindo as perguntas como uma lista de dicionários
    perguntas = [
        {
            "pergunta": "Comunicacao e Trabalho em Equipe",
            "descricao": "Em uma escala de 1 a 5, como voce avalia sua propria capacidade de se comunicar efetivamente e colaborar com outros membros da equipe para alcancar objetivos em projetos de trabalho em equipe?",
            "resposta": None
        },
        {
            "pergunta": "Engajamento e Proatividade",
            "descricao": "Em uma escala de 1 a 5, como voce avalia o seu proprio nivel de engajamento e proatividade no ambiente de trabalho?",
            "resposta": None
        },
        {
            "pergunta": "Conhecimento e Aplicabilidade",
            "descricao": "Em uma escala de 1 a 5, como voce avalia seu proprio nivel de conhecimento tecnico em relacao as tecnologias e ferramentas usadas no trabalho e sua capacidade de aplica-lo em projetos e tarefas especiificas relacionadas ao trabalho?",
            "resposta": None
        },
        {
            "pergunta": "Entrega de Resultados com Valor Agregado",
            "descricao": "Em uma escala de 1 a 5, como voce avalia sua propria capacidade de entregar resultados com valor agregado em projetos e tarefas relacionadas ao trabalho?",
            "resposta": None
        },
        {
            "pergunta": "Autogestao de Atividades",
            "descricao": "Em uma escala de 1 a 5, como voce avalia sua propria capacidade de gerenciar suas proprias atividades e prazos para atingir as metas do projeto?",
            "resposta": None
        }
    ]

    # Loop para obter as respostas do participante
    for pergunta in perguntas:
        print(pergunta["descricao"])
        pergunta["resposta"] = obter_resposta()

    # Exibindo os resultados
    print("Resultado da Avaliação:")
    for pergunta in perguntas:
        print(f"Pergunta: {pergunta['pergunta']}")
        print(f"Descrição: {pergunta['descricao']}")
        print(f"Resposta: {pergunta['resposta']}")
        print("-" * 30)
                 
    # Salvar as respostas em um arquivo JSON
    with open("respostas_avaliacao.json", "w") as arquivo:
        json.dump(perguntas, arquivo, indent=5)

        print("Respostas salvas em respostas_avaliacao.json.")
     
    
elif entrada_avaliacao == '2':
    print("Opção 2 selecionada. Sair.")
else:
    print("Opção inválida. Por favor, escolha uma opção válida.")


    








