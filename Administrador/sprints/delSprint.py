import json

caminho_sprint = "././data/sprint.json"
caminho_turma = "././data/turmas.json"

def delSprint():
    #Visualizar Turma
    arqv_turmas = open(caminho_turma)
    read_arqv_turmas = json.load(arqv_turmas)
    print("\nVisualizar Turmas:")
    y = 1
    for turma in read_arqv_turmas:
        print(y, "-", turma.get('identificacao'))
        y += 1
    while True:
        try:
            num_turma = int(input('\n Digite de qual turma deseja vizualizar as sprints:'))
            if num_turma > y - 1 or num_turma == 0:
                raise ValueError
            else:
                break
        except ValueError:
            print("\nValor inválido")
            
    turma_escolhida = read_arqv_turmas[num_turma-1]
    id_turma = turma_escolhida['id_turma']

    #Visualizar Sprints
    arqv_sprints = open(caminho_sprint)
    read_arqv_sprint = json.load(arqv_sprints)

    print("\nQual Sprint deseja deletar: ")
    sprints_turma = []
    for sprint in read_arqv_sprint:
        if sprint.get('id_turma') == id_turma:
            sprints_turma.append(sprint)

    x = 1
    for sprint in sprints_turma:
        print(f"{x} - {sprint.get('identificacao')}")
        x += 1
        
    while True:
        try:
            num_sprint = int(input('\nDigite aqui: '))
            if num_sprint > x-1 or num_sprint == 0:
                raise ValueError
            else:
                break
        except ValueError:
            print('\nValor inválido')
        
    sprint_del = sprints_turma[num_sprint - 1]
    read_arqv_sprint.remove(sprint_del)
    
    with open(caminho_sprint, 'w') as output:
        json.dump(read_arqv_sprint, output)
    output.close()
    print('\nSprint excluída!')
    

