import pandas as pd
import json

def dashturma():
    while True:
        print("Dashboard turmas!")
        competencias = ["Comunicacão e Trabalho em Equipe", "Engajamento e Proatividade", "Conhecimento e Aplicabilidade", "Entrega de Resultados com Valor Agregado", "Autogestão de Atividades"]
        arqv_turmas = open('././data/turmas.json')
        turmas = json.load(arqv_turmas) #load() - leitura do arquivo
        
        arqv_resp_auto = open('././data/respostas_autoAvaliacao.json')
        autoavaliacao = json.load(arqv_resp_auto)

        arqv_resp_grupo = open('././data/respostas_grupoAvaliacao.json')
        grupos = json.load(arqv_resp_grupo)

        arqv_sprint = open('././data/sprint.json')
        sprints = json.load(arqv_sprint)

        for turma in turmas:
            if sprints['id_turma'] == id_turma:
                id_turma = int(sprint['id_turma'])

        sprints_turma = []
        for sprint in sprints:
            if int(sprint['id_turma']) == id_turma:
                sprints_turma.append(sprint)
        x = 1
        for comp in competencias:
            dados_colunas = {}
            if sprints_turma > 0:
                for turma in sprints_turma:
                    comp1 = 0
                    comp2 = 0
                    comp3 = 0
                    comp4 = 0
                    comp5 = 0
                    for resp in autoavaliacao:
                        if resp['id_sprint'] == sprints['id_sprint'] and sprints['id_turma'] == turmas['id_turma'] == str(x):
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
                        if resp['id_sprint'] == sprints['id_sprint'] and sprints['id_turma'] == turmas['id_turma'] == str(x):
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
                print('Sem turmas!')
                break
            
        break

