import json
import os
from datetime import datetime, timedelta

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
    print("\033[32;1mCONTROLE DE SPRINTS\033[m")
    print('\n\033[3;1mVocê escolheu a opção:\033[m \033[4;33m"Criar Sprint"\033[m\n')
    print("\033[32;1mTurmas:\033[m\n")
    x = 1
    for turma in read_arqv_turmas:
        print(f"\033[33;4m{x}\033[m - {turma.get('identificacao')}")
        x = x + 1
    print("\033[33;4m0\033[m - Voltar")

    while True:
        try:
            op = int(input('\n\033[36;1mDigite qual turma deseja inserir uma sprint:\033[m'))  # deixar apenas número inteiro
            if op in range(1, x):
                break
            else:
                if op == 0:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return
                raise ValueError
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n\033[31;1mOpção inválida! Tente novamente!\033[m\n')

    turma_escolhida = read_arqv_turmas[op - 1]
    id_turma = turma_escolhida['id_turma']
    

    identificacao_sprint = input("\033[36;1mEntre com a identificacao da sprint:\033[m ")
    
    while True:
        data_inicio = str(input('\033[36;1mEntre com a data inicial (dd/mm/aaaa):\033[m'))
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
                    print('\033[31;1mData inválida\033[m\n')
                else:
                    print('\033[32;1mData inicial salva\033[m')
                break
            else:
                print('\033[31;1mFormato de data inválida digite somente números\033[m\n')
        else: 
            print('\033[31;1mData inválida\033[Data inválida digite conforme dd/mm/aaaa\033[m\n')

    # Solicitar a data final até que seja maior que a data de inicio
    while True:

        data_final = str(input('\033[36;1mEntre com a data final (dd/mm/aaaa):\033[m'))

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
                    print('\033[31;1mData inválida\033[m\n')
                else:
                    if data_inicio >= data_final:
                        print('\033[31;1mData inicial maior que a data final \nDigite uma data maior que a inicial\033[m\n')
                    else:

                        print('\033[32;1mData final Salva\033[m')
                        break
            else:
                print('\033[31;1mFormato de data inválida, digite somente numeros\033[m\n')
        else: 
            print('\033[31;1mData inválida digite conforme dd/mm/aaaa\033[m\n')

    def dataResponderAvaliacao():
        while True:
                data = input('\n\033[36;1mDigite a data final para responder a avaliação(dd/mm/aaaa): \033[m')
                try:
                    data = datetime.strptime(data, '%d/%m/%Y')
                    data_final_sprint = datetime.strptime(data_final, '%d/%m/%Y')
                    limite_dias = timedelta(days=5)
                    data_final_resposta = limite_dias + data_final_sprint
                    if data > data_final_sprint and data <= data_final_resposta:
                        data_responder_sprint = data.strftime("%d/%m/%Y")
                        return data_responder_sprint
                    else:
                        print("\n\033[31;1mData precisa ser no máximo 5 dias após o final da sprint.\033[m")
                except ValueError:
                    print('\n\033[31;1mFormato de data inválido ou data inválida.\033[m\n')

    # Aqui solicita a data final para responder a avaliação 
    data_final_avaliacao = dataResponderAvaliacao()

    maior_id_sprint = 0
    for sprint in sprints:
        if maior_id_sprint < int(sprint['id_sprint']):
            maior_id_sprint = int(sprint['id_sprint'])

    nova_sprint = {
        'id_sprint': maior_id_sprint + 1,
        'identificacao': identificacao_sprint,
        'id_turma': id_turma,
        'inicio': data_inicio,
        'final' : data_final,
        'final_avaliacao': data_final_avaliacao
        
    }
    
    sprints.append(nova_sprint)

    with open(caminho_sprint, 'w') as f:
        # Escrevendo os dados atualizados no arquivo
        json.dump(sprints, f)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\033[32;1mNOVA SPRINT CRIADA\033[m')


