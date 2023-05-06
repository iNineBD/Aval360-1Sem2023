import json

# Função para editar um time
def editusuarios():
    #Visualizar Turmas:
        arqv_turmas = open('././data/turmas.json')
        read_arqv_turmas = json.load(arqv_turmas) #load() - leitura do arquivo
        print("Turmas:\n")
        x = 1
        for turma in read_arqv_turmas:
            print(f"{x} - {turma.get('identificacao')}")
            x = x+1
        while True:
            try:
                num_turmas = int(input('\nDigite qual Turma deseja visualizar os Times: '))  #deixar apenas número inteiro
                break
            except ValueError:
                print('\nOpção inválida! Tente novamente!\n')
        
        turma_escolhida = read_arqv_turmas[num_turmas - 1]
        id_turma = turma_escolhida['id_turma']
    #Visualizar times     
        while True:
            if num_turmas < x:
                #load() - leitura do arquivo
                arqv_times = open('./data/times.json')
                read_arqv_times = json.load(arqv_times) 
            
                y = 1
                for time in read_arqv_times:
                    if time.get('id_turma') == id_turma:
                        print(f"{y} - {time.get('identificacao')}")
                        y = y + 1
                break
            
            
            else:
                print('\nValor inválido')

        arqv_usuarios = open('././data/usuarios.json')
        read_arqv_usuarios = json.load(arqv_usuarios)



" Digite qual Time deseja visualizar os Usuarios:"

    #    arqv_usuarios = open('././data/usuarios.json')
    #    read_arqv_usuarios = json.load(arqv_usuarios)
#
    #    print("\nUsuários:\n")
    #    indice_vs_usuario_id = {}
    #    z = 0
    #    for usuario in read_arqv_usuarios:
    #        print(z + 1, "-", usuario.get("identificacao"))
    #        indice_vs_usuario_id[str(z)] = usuario.get("id_usuario")
    #        z += 1
#

#        z = 0
#        for usuario in read_arqv_usuarios:
#            print(z + 1, "-", usuario.get("identificacao"))
#            indice_vs_usuario_id[str(z)] = usuario.get("id_usuario")
#            z += 1
#
#
#if time.get("id_turma") == id_turma:
#            print(y, "-", time.get("identificacao"))
#            indice_vs_time_id[str(y)] = time.get("id_time")
#            y += 1
#            x = True