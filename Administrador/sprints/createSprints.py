import json
import os

caminho_sprint = "././data/sprint.json"
caminho_turmas = "././data/turmas.json"

# Método para criar sprints
def createSprints():
        
    # Visualizar Turmas
    # Verifica se o arquivo JSON já existe
    if os.path.exists(caminho_sprint):
        # Se existir, carrega os usuários existentes
        with open(caminho_sprint, 'r') as spr:
            sprints = json.load(spr)
    else:
        # Se não existir, cria uma lista vazia
        sprints = []
    




    # Visualizar Turmas
    # Verifica se o arquivo JSON já existe
    if os.path.exists(caminho_turmas):
        # Se existir, carrega os usuários existentes
        with open(caminho_turmas, 'r') as arquivo:
            read_arqv_turmas = json.load(arquivo)
    else:
        # Se não existir, cria uma lista vazia
        read_arqv_turmas = []
    
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
    
    while True:
        data_inicio = str(input('Entre com a data inicial (dd/mm/aaaa):'))
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
                    print('Data inválida')
                else:
                    print('Data inicial salva')
                break
            else:
                print('Formato de data inválida digite somente numeros')
        else: 
            print('Data inválida digite conforme dd/mm/aaaa ')
            
        

    # Solicitar a data final até que seja maior que a data de inicio
    while True:
        data_final = str(input('Entre com a data final (dd/mm/aaaa):'))
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
                    print('Data inválida')
                else:
                    if data_inicio >= data_final:
                        print('Data inicial maior que a data final \nDigite uma data maior que a inicial')
                    else:
                        print('Data final Salva')
                        break
            else:
                print('Formato de data inválida digite somente numeros')
        else: 
            print('Data inválida digite conforme dd/mm/aaaa ')
            
            


    maior_id_sprint = 0
    for sprint in sprints:
        if maior_id_sprint < int(sprint['id_sprint']):
            maior_id_sprint = int(sprint['id_sprint'])

    nova_sprint = {
        'id_sprint': maior_id_sprint + 1,
        'identificacao': identificacao_sprint,
        'id_turma': id_turma,
        'inicio': data_inicio,
        'final' : data_final
        
    }
    
    sprints.append(nova_sprint)

    with open(caminho_sprint, 'w') as f:
        # Escrevendo os dados atualizados no arquivo
        json.dump(sprints, f)

    print('Nova sprint criada!')

