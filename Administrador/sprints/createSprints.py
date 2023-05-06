import json
import os

caminho_sprint = "././data/sprint.json"

# Método para criar sprints
def createSprints():
    with open(caminho_sprint, 'r') as spr:
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
            if op in range(1, x):
                break
            else:
                raise ValueError
        except ValueError:
            print('\nOpção inválida! Tente novamente!\n')

    turma_escolhida = read_arqv_turmas[op - 1]
    id_turma = turma_escolhida['id_turma']

    identificacao_sprint = input("Entre com a identificacao da sprint: ")

    ano = int(input("Digite o Ano: "))
    mes = int(input("Digite o Mês: "))
    dia = int(input("Digite o Dia: "))
    valida = True
    if ano < 1:
        valida = False
    elif mes < 1 or mes > 12 or dia < 1 or dia > 31:
        valida = False
    elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
        valida = False
    elif mes == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
            if dia > 29:
                valida = False
        else:
            if dia > 28:
                valida = False
    else:
        valida = True

    if valida:
        print("DATA VALIDA")
    else:
        print("DATA INVALIDA")

    inicio = f"({dia}/{mes}/{ano})"

    # Solicitar a data final até que seja maior que a data de inicio
    while True:
        final = str(input("Entre com a data final da sprint: "))
        dia_final, mes_final, ano_final = map(int, final.split('/'))

        if (ano_final, mes_final, dia_final) > (ano, mes, dia):
            break
        else:
            print("A data final deve ser maior que a data de início.")

    print("DATA FINAL VÁLIDA")

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

