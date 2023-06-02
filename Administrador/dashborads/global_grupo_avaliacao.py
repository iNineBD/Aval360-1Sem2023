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
                print('\n\033[31mOPÇÃO INVÁLIDA!\033[m\n\033[3mNão existe avaliação para ser exibida!\033[m') 
                #print("\033[Não exista avaliação para ser mostrada\n")
                print('------------------------------------------')
                return False
            
    if verificacao() == True:
                    
        def dashGlobal():
            
            with open (local_turmas,'r') as arquivo_turmas:
                turmas = json.load(arquivo_turmas)
            
            with open (local_sprints,'r') as arquivo_sprints:
                sprints = json.load(arquivo_sprints)
                
            with open(local_resposta_autoavaliacao) as arquivo_autoavaliação:
                resposta_autoavaliacao = json.load(arquivo_autoavaliação)
                
            with open(local_resposta_avaliacao) as arquivo_avaliacao:
                resposta_avaliacao = json.load(arquivo_avaliacao)
            
            id_turmas = list()
            
            for turma in turmas:
                if turma not in id_turmas:
                    id_turmas.append(turma.get('id_turma'))
            
            competencia = ["Comunicacão e Trabalho em Equipe", "Engajamento e Proatividade", "Conhecimento e Aplicabilidade", "Entrega de Resultados com Valor Agregado", "Autogestão de Atividades"]
            id_sprints = list()
            try:
                for sprint in sprints:
                    if sprint.get('id_turma') in id_turmas:
                        id_sprints.append(sprint.get('id_sprint'))
                                
                num_comp = 1
                for comp in competencia:
                    dados_coluna = {}
                    if len(id_sprints) > 0:
                        sum_comp_1 = 0
                        sum_comp_2 = 0
                        sum_comp_3 = 0
                        sum_comp_4 = 0
                        sum_comp_5 = 0
                        
                        for resposta_auto in resposta_autoavaliacao:
                            if resposta_auto.get('id_sprint') in id_sprints and resposta_auto.get('ip') == str(num_comp):
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
                            if resposta_grupo.get('id_sprint') in id_sprints and resposta_grupo.get('ip') == str(num_comp):
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
                        dados_coluna['\033[36;1mSprints\033[m'] = coluna
                    
                    num_comp +=1
                    df = pandas.DataFrame(dados_coluna, index = ['Excelente', 'Muito bom', 'Bom', 'Razoável', 'Ruim'])
                    print(f"\n\033[32;3;1m{comp} (%)\033[m\n")
                    #print(f"\n{comp} (%)\n")
                    print(df.round(2))
                    #print('\n-----------------------\n')
                            
                if len(id_sprints) <= 0:
                    print('\n\033[31mOPÇÃO INVÁLIDA!\033[m\n\033[3mSem sprints para essa Turma!\033[m')
                    #print('Sem sprints para essa turma')
            except ValueError:
                print('\n\033[31mOPÇÃO INVÁLIDA!\033[m\n\033[3mNão existe Time nessa Turma para exibição de Dashboard\033[m')
                #print("\nNão existe time nessa turma para mostrar um dashboard")
                                        
        dashGlobal()


