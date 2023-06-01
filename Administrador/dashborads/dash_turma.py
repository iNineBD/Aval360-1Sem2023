import pandas as pd
import json
import os

def dashturma():
    if os.path.exists('././data/respostas_autoAvaliacao.json') and os.path.exists('././data/respostas_grupoAvaliacao.json'):
        print("\033[32;1mTELA DE DASHBOARD - TURMAS\033[m\n")
        #print("Dashboard turmas!")
        competencias = ["Comunicacão e Trabalho em Equipe", "Engajamento e Proatividade", "Conhecimento e Aplicabilidade", "Entrega de Resultados com Valor Agregado", "Autogestão de Atividades"]
        arqv_turmas = open('././data/turmas.json')
        turmas = json.load(arqv_turmas) #load() - leitura do arquivo
        
        arqv_resp_auto = open('././data/respostas_autoAvaliacao.json')
        autoavaliacao = json.load(arqv_resp_auto)

        arqv_resp_grupo = open('././data/respostas_grupoAvaliacao.json')
        grupos = json.load(arqv_resp_grupo)

        arqv_sprint = open('././data/sprint.json')
        sprints = json.load(arqv_sprint)

        x = 1
        for turma in turmas:
            print(f"{x} - {turma.get('identificacao')}")
            x += 1
        
            
        while True:
            try:
                entrada_turma = int(input(str("\n\033[36mDigite qual Turma acima deseja visualizar: ")))
                if entrada_turma > x-1:
                    raise ValueError
                    #print ("Essa turma não existe")
                else: 
                    turma_escolhida = turmas[entrada_turma - 1]
                    id_turma = turma_escolhida['id_turma']

                sprints_turma = []
                for sprint in sprints:
                    if int(sprint['id_turma']) == int(id_turma):
                        sprints_turma.append(sprint)
                x = 1
                for comp in competencias:
                    dados_colunas = {}
                    if len(sprints_turma) > 0:
                        for sprint in sprints_turma:
                            comp1 = 0
                            comp2 = 0
                            comp3 = 0
                            comp4 = 0
                            comp5 = 0
                            for resp in autoavaliacao:
                                if resp['id_sprint'] == sprint['id_sprint'] and sprint['id_turma'] == id_turma and resp['ip'] == str(x):
                                    if resp['resp'] == "1":
                                        comp1 += 1
                                    elif resp['resp'] == "2":
                                        comp2 += 1
                                    elif resp['resp'] == "3":
                                        comp3 += 1
                                    elif resp['resp'] == "4":
                                        comp4 += 1
                                    elif resp['resp'] == "5":
                                        comp5 += 1
                            for resp in grupos:
                                if resp['id_sprint'] == sprint['id_sprint'] and sprint['id_turma'] == id_turma and resp['ip'] == str(x):
                                    if resp['resp'] == "1":
                                        comp1 += 1
                                    elif resp['resp'] == "2":
                                        comp2 += 1
                                    elif resp['resp'] == "3":
                                        comp3 += 1
                                    elif resp['resp'] == "4":
                                        comp4 += 1
                                    elif resp['resp'] == "5":
                                        comp5 += 1
                            coluna = [(comp1), (comp2), (comp3), (comp4), (comp5)]
                            total = sum(coluna)
                            
                            if total != 0:
                                coluna = [(comp5/total)*100, (comp4/total)*100, (comp3/total)*100, (comp2/total)*100, (comp1/total)*100]
                            dados_colunas[sprint['identificacao']] = coluna
                        
                        x += 1
                        df = pd.DataFrame(dados_colunas, index = ['Excelente', 'Muito bom', 'Bom', 'Razoável', 'Ruim'])
                        print(f"\n\033[32;3;1m{comp} (%)\033[m\n")
                        print(df.round(2))
                        print('\n------------------------------------')
                        print("")
                    else:
                        print('Sem sprints!')
                break
            except ValueError:
                print('\n\033[31mOPÇÃO INVÁLIDA!\033[m\n\033[3mEssa Turma não existe!\033[m') 
    else:
        print('\n\033[31mOPÇÃO INVÁLIDA!\033[m\n\033[3mNão existe avaliação para ser exibida!\033[m')
        #print("Não exista avaliação para ser mostrada\n")
        

