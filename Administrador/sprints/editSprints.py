import json
import os

caminho_sprint = "././data/sprint.json"
caminho_turma = "././data/turmas.json"

# Método para criar sprints
def editSprints():
    with open(caminho_turma, 'r') as turmas:
        turmas = json.load(turmas)

    print('\n\033[3;1mVocê escolheu a opção:\033[m \033[4;33m"Editar Sprint"\033[m\n')
    print("\n\033[36;1mTurmas:\033[m\n")
    x = 1
    for turma in turmas:
        print(f'\033[33;4m{x}\033[m - {turma["identificacao"]}')
        x +=1

    print("\033[33;4m0\033[m - Voltar")

    while True:
        try:
            indice_turma_escolhida = int(input('\033[36;1m\nDigite a turma referente a sprint desejada: \033[m')) - 1

            if indice_turma_escolhida >= (x - 1):
                raise ValueError
            else:
                if indice_turma_escolhida +1 == 0:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return
                break
        except ValueError:

            print('\n\033[31mVALOR INVÁLIDO!\033[m\n\033[3mTente novamente!\033[m')

    
    
    id_turma = str(turmas[indice_turma_escolhida]["id_turma"])
    
    with open(caminho_sprint, 'r') as sprints:
        sprints = json.load(sprints)
    
    sprints_turmas = []
    for sprint in sprints:
        if sprint['id_turma'] == id_turma:
            sprints_turmas.append(sprint)
    
    y = 1
    for sprint in sprints_turmas:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n\033[36;1mSprints:\033[m\n")
        print(f'\033[33;4m{y}\033[m - {sprint["identificacao"]}')
        y+=1
    print('\033[33;4m0\033[m  - Voltar')
    
    while True:
        try:
            a = int(input('\033[36;1m\nDigite a sprint que você deseja editar: \033[m')) - 1
            if a >= (y - 1):
                raise ValueError
            else:
                if a + 1 == 0:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return
                break
        except ValueError:

            print('\n\033[31mVALOR INVÁLIDO!\033[m\n\033[3mTente novamente!\033[m')
    
    
    id_sprint = sprints_turmas[a]["id_sprint"]
    indice_sprint_escolhida = sprints.index(sprints_turmas[a])
    
    del(sprints[indice_sprint_escolhida])
    
    identificacao_sprint = input("\033[36;1mEntre com a identificacao da sprint: \033[m")
    while True:
        data_inicio = str(input('\033[36;1mEntre com a data inicial (dd/mm/aaaa): \033[m'))
        if len(data_inicio) == 10 and data_inicio[2] == '/' and data_inicio[5] == '/':
            dia = (data_inicio.split('/')[0]) #// 1000000 
            mes = (data_inicio.split('/')[1])#%1000000//10000
            ano = (data_inicio.split('/')[2]) #% 10000
            
            if dia.isdigit() and mes.isdigit() and ano.isdigit():
                dia = int(dia)
                mes = int(mes)
                ano = int(ano)
            
            
                if ano >= 1:
                    vd = 1
                    if mes < 1 or mes > 12 or dia < 1 or dia > 31:
                        vd = 0
                    elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
                        vd = 0
                    elif mes == 2:
                        if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
                            if dia > 29:
                                vd = 0
                        else:
                            if dia > 28:
                                vd = 0
                else:
                    vd = 0
                if vd == 0:
                    print('\033[31;1mData inválida\033[m')
                else:
                    print('\033[32;1mData inicial salva\033[m')
                break
            else:

                print('\033[31;1mFormato de data inválida digite somente números\033[m')
        else: 
            print('\033[31mData inválida, digite conforme (dd/mm/aaaa) \033[m')

    # Solicitar a data final até que seja maior que a data de inicio
    while True:
        data_final = str(input('\033[36;1mEntre com a data final (dd/mm/aaaa): \033[m'))

        if len(data_final) == 10 and data_final[2] == '/' and data_final[5] == '/':
            dia = (data_final.split('/')[0]) #// 1000000
            mes = (data_final.split('/')[1])#%1000000//10000
            ano = (data_final.split('/')[2])# % 10000
            
            if dia.isdigit() and mes.isdigit() and ano.isdigit():
                dia = int(dia)
                mes = int(mes)
                ano = int(ano)
            
            
                if ano >= 1:
                    vd = 1
                    if mes < 1 or mes > 12 or dia < 1 or dia > 31:
                        vd = 0
                    elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
                        vd = 0
                    elif mes == 2:
                        if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
                            if dia > 29:
                                vd = 0
                        else:
                            if dia > 28:
                                vd = 0
                else:
                    vd = 0
                if vd == 0:
                    print('\033[31;1mData inválida\033[m')
                else:
                    if data_inicio >= data_final:
                        print('\033[31;1mData inicial maior que a data final \nDigite uma data maior que a inicial\033[m')
                    else:

                        print('\n\033[32;1mData final Salva\033[m')
                        break
            else:
                print('\033[31mFormato de data inválida, digite somente números\033[m')
        else: 
            print('\033[31;1mData inválida, digite conforme (dd/mm/aaaa) \033[m')

            
    nova_sprint = {
        'id_sprint': id_sprint,
        'identificacao': identificacao_sprint,
        'id_turma': id_turma,
        'inicio': data_inicio,
        'final' : data_final
        
    }
    
    sprints.append(nova_sprint)
    
    with open(caminho_sprint, "w") as spr:
        json.dump(sprints, spr)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n\033[1;32mSPRINT EDITADA COM SUCESSO\033")