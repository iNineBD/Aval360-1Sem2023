import json
import os
caminho_sprint = "././data/sprint.json"
# Método para criar sprints
def createSprints():
    with open (caminho_sprint, 'r') as spr:
        sprints = json.load(spr)

    # Visualizar Turmas
    arqv_turmas = open('././data/turmas.json')
    read_arqv_turmas = json.load(arqv_turmas)  # load() - leitura do arquivo
    print("\nVisualizar Turmas:")
    x = 1
    for turma in read_arqv_turmas:
        print(f"{x} - {turma.get('identificacao')}")
        x = x + 1
    while True:
        try:
            op = int(input('\nDigite qual turma deseja inserir uma sprint: '))  # deixar apenas número inteiro
            if op in range (1,x) :
                break
            else:
                raise ValueError
        except ValueError:
            print('\nOpção inválida! Tente novamente!\n')

    turma_escolhida = read_arqv_turmas[op - 1]
    id_turma = turma_escolhida['id_turma']

    identificacao_sprint = input("Entre com a identificacao da sprint: ")
    while True:
        try:
            numero_da_sprint = int(input("Entre com o numero da sprint: "))
            break
        except ValueError:
            print('Insira um valor inteiro!')
    inicio = str(input("Entre com a data inicial da sprint"))
    
    final = str(input("Entre com a data final da sprint"))
    

    maior_id_sprint = 0
    for sprint in sprints:
        if maior_id_sprint < int(sprint['id_sprint']):
            maior_id_sprint = int(sprint['id_sprint'])

    nova_sprint = {
        'id_sprint': maior_id_sprint + 1,
        'identificacao': identificacao_sprint,
        'id_turma': id_turma,
        'inicio': inicio,
        'final' : final
        
        
    }
    sprints.append(nova_sprint)

    with open(caminho_sprint, 'w') as f:
        # Escrevendo os dados atualizados no arquivo
        json.dump(sprints, f)

    print('\nTime sprint!')

