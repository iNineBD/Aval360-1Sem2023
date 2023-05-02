import json

caminho_sprint = "././data/sprint.json"

#Visualizar Sprints


def delSprint():
    arqv_sprints = open(caminho_sprint)
    read_arqv_sprint = json.load(arqv_sprints)
    print("Qual Sprint deseja deletar: ")
    x = 1
    for sprint in read_arqv_sprint:
        print(f"{x} - {sprint.get('identificacao')}")
        x +=1
    while True:
        try:
            num_sprint = int(input('\nDigite aqui: '))
            if num_sprint > x -1:
                raise ValueError
            else:
                break
        except ValueError:
            print('\nValor inválido')
            return delSprint()

    sprint_escolhida = read_arqv_sprint[num_sprint-1]
   
    sprint_del = sprint_escolhida
    read_arqv_sprint.remove(sprint_del)

    with open(caminho_sprint, 'w') as output:
        json.dump(read_arqv_sprint, output)
    output.close()
    print('\nTurma excluída!')

