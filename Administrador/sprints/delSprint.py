import json
import os

caminho_sprint = "././data/sprint.json"
caminho_turma = "././data/turmas.json"

def delSprint():
    #Visualizar Turma
    arqv_turmas = open(caminho_turma)
    read_arqv_turmas = json.load(arqv_turmas)
    
    print('\n\033[3;1mVocê escolheu a opção:\033[m \033[4;33m"Deletar Sprint"\033[m\n')
    print("\n\033[32;1mTurmas:\033[m")
    y = 1
    for turma in read_arqv_turmas:
        print(f"\033[33;4m{y}\033[m - {turma.get('identificacao')}")
        y += 1
    print("\033[33;4m0\033[m - Voltar\n")

    while True:
        try:
            num_turma = int(input('\n\033[36mDigite de qual turma deseja vizualizar as sprints:\033[m'))
            if num_turma > y - 1:
                raise ValueError
            else:
                if num_turma == 0:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return
                break
        except ValueError:
            print("\n\033[31mValor inválido\033[m")
            
    turma_escolhida = read_arqv_turmas[num_turma-1]
    id_turma = turma_escolhida['id_turma']

    #Visualizar Sprints
    arqv_sprints = open(caminho_sprint)
    read_arqv_sprint = json.load(arqv_sprints)

    print("\n\033[36mQual Sprint deseja deletar: \033[m")
    sprints_turma = []
    for sprint in read_arqv_sprint:
        if sprint.get('id_turma') == id_turma:
            sprints_turma.append(sprint)

    x = 1
    for sprint in sprints_turma:
        print(f"\033[33;4m{x}\033[m - {sprint.get('identificacao')}")
        x += 1
    print("\033[33;4m0\033[m - Voltar\n")

    while True:
        try:
            num_sprint = int(input('\033[36m\nDigite aqui: \033[m'))
            if num_sprint > x-1:
                raise ValueError
            else:
                if num_sprint == 0:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return
                break
        except ValueError:
            print('\033[31m\nValor inválido\033[m')
        
    sprint_del = sprints_turma[num_sprint - 1]
    read_arqv_sprint.remove(sprint_del)
    
    with open(caminho_sprint, 'w') as output:
        json.dump(read_arqv_sprint, output)
    output.close()
    print('\033[32;1m\nSprint excluída!\033[m')
    

