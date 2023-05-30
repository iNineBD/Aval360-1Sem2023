import pandas
import json
import os

local_sprints = '././data/sprint.json'
local_turmas =  '././data/turmas.json'
local_resposta_autoavaliacao = '././data/respostas_autoAvaliacao.json'
local_resposta_avaliacao = '././data/respostas_grupoAvaliacao.json'

def visualizarDashGlobal():
    
    def verificacao():
        while True:
            if os.path.exists(local_resposta_avaliacao):
                return True 

            else:
                print("Não exista avaliação para ser mostrada\n")
                print('------------------------------------------')
                return False
            
    if verificacao() == True:
                
        def visualizarTurmas():
            
            with open (local_turmas,'r') as arquivo_turmas:
                turmas = json.load(arquivo_turmas)

            print("\nVisualizar Turmas:")
            x = 1
            for name in turmas:
                print(f"{x} - {name['identificacao']}")
                x = x+1
            print('0 - Voltar')
            
            while True:
                try:
                    num_turmas = int(input('\nDigite qual turma deseja visualizar: '))  #deixar apenas número inteiro
                    if num_turmas > x-1:
                        print('\nEssa turma não existe')
                    elif num_turmas == 0:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        return num_turmas
                    else:
                        break    
                except ValueError:
                    print('\nOpção inválida! Tente novamente!')

            os.system('cls' if os.name == 'nt' else 'clear')
            turma_escolhida = turmas[num_turmas - 1]
            id_turma = turma_escolhida.get('id_turma')
            return id_turma
        
        def dashGlobal(turma):
            
            with open (local_sprints,'r') as arquivo_sprints:
                sprints = json.load(arquivo_sprints)
                
            with open(local_resposta_autoavaliacao) as arquivo_autoavaliação:
                resposta_autoavaliacao = json.load(arquivo_autoavaliação)
                
            with open(local_resposta_avaliacao) as arquivo_avaliacao:
                resposta_avaliacao = json.load(arquivo_avaliacao)
            
            competencia = ["Comunicacão e Trabalho em Equipe", "Engajamento e Proatividade", "Conhecimento e Aplicabilidade", "Entrega de Resultados com Valor Agregado", "Autogestão de Atividades"]
            id_sprints = list()
            sprints_turma = list()
            try:
                for sprint in sprints:
                    if sprint.get('id_turma') == turma:
                        sprints_turma.append(sprint)
                        id_sprints.append(sprint.get('id_sprint'))
                                
                num_comp = 1
                for comp in competencia:
                    dados_coluna = {}
                    if len(id_sprints) > 0:
                        for sprint in sprints_turma:
                            sum_comp_1 = 0
                            sum_comp_2 = 0
                            sum_comp_3 = 0
                            sum_comp_4 = 0
                            sum_comp_5 = 0
                            
                            for resposta_auto in resposta_autoavaliacao:
                                if resposta_auto.get('id_sprint') in id_sprints and resposta_auto.get('ip') == str(num_comp) and sprint.get('id_sprint') == resposta_auto.get('id_sprint'):
                                    if resposta_auto.get('resp') == '1':
                                        sum_comp_1 += 1
                                    elif resposta_auto.get('resp') == '2':
                                        sum_comp_2 += 1
                                    elif resposta_auto.get('resp') == '3':
                                        sum_comp_3 += 1
                                    elif resposta_auto.get('resp') == '4':
                                        sum_comp_4 += 1
                                    elif resposta_auto.get('resp') == '5':
                                        sum_comp_5 += 1
                                        
                            for resposta_grupo in resposta_avaliacao:
                                if resposta_grupo.get('id_usuario_respondeu') in id_sprints and resposta_grupo.get('ip') == str(num_comp) and sprint.get('id_sprint') == resposta_auto.get('id_sprint'):
                                    if resposta_grupo.get('resp') == '1':
                                        sum_comp_1 += 1
                                    elif resposta_grupo.get('resp') == '2':
                                        sum_comp_2 += 1
                                    elif resposta_grupo.get('resp') == '3':
                                        sum_comp_3 += 1
                                    elif resposta_grupo.get('resp') == '4':
                                        sum_comp_4 += 1
                                    elif resposta_grupo.get('resp') == '5':
                                        sum_comp_5 += 1
                                    
                            coluna = [(sum_comp_5), (sum_comp_4), (sum_comp_3), (sum_comp_2), (sum_comp_1)]
                            total = sum(coluna)
                            
                            if total != 0:
                                coluna = [(sum_comp_5/total)*100, (sum_comp_4/total)*100, (sum_comp_3/total)*100, (sum_comp_2/total)*100, (sum_comp_1/total)*100]
                            dados_coluna[sprint.get('identificacao')] = coluna
                        
                        num_comp +=1
                        df = pandas.DataFrame(dados_coluna, index = ['Excelente', 'Muito bom', 'Bom', 'Razoável', 'Ruim'])
                        print(f"\n{comp} (%)\n")
                        print(df.round(2))
                        print('\n-----------------------\n')
                            
                if len(id_sprints) <= 0:
                    print('Sem sprints para essa turma')
            except ValueError:
                print("\nNão existe time nessa turma para mostrar um dashboard")
        
        
        turma = visualizarTurmas()
        
        if turma != 0:                          
            dashGlobal(turma)
            opcao = int(input('\n0 - Voltar\n\nDigite aqui: '))
            while True:
                if opcao == 0:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
                else:
                    print('\nNúmero inválido')
                    opcao = int(input('\n0 - Voltar\n\nDigite aqui: '))
            os.system('cls' if os.name == 'nt' else 'clear')

