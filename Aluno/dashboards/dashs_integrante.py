import json
import os
import pandas as pd

local_resposta_auto = '././data/respostas_autoAvaliacao.json'
local_resposta_grupo = '././data/respostas_grupoAvaliacao.json'
local_usu = '././data/usuarios.json'
local_sprints = '././data/sprint.json'
local_time = '././data/times.json'
competencias = ["Comunicacão e Trabalho em Equipe", "Engajamento e Proatividade", "Conhecimento e Aplicabilidade", "Entrega de Resultados com Valor Agregado", "Autogestão de Atividades"]

def dashs_integrante(id_usuario, id_time):
    while True:
        if os.path.exists(local_resposta_auto) and os.path.exists(local_resposta_grupo):
            with open(local_resposta_auto) as rsp_auto:
                resp_auto = json.load(rsp_auto)
            with open(local_resposta_grupo) as rsp_grupo:
                resp_grupo = json.load(rsp_grupo)
            with open(local_sprints) as sp:
                sprints = json.load(sp)
            with open(local_time) as tm:
                times = json.load(tm)
        else:
            print("As avaliações ainda não começaram! Volte mais tarde!")
            break
        # pegandp o id da turma do usuario
        for time in times:
            if time['id_time'] == id_time:
                id_turma = int(time['id_turma'])
        
        # pegando as sprints dessa turma
        sprints_turma = []
        for sprint in sprints:
            if int(sprint['id_turma']) == id_turma:
                sprints_turma.append(sprint)
                
        indice_comp = 1
        for comp in competencias:
            dados_colunas = {}
            if len(sprints_turma) > 0:
                for sprint in sprints_turma:
                    likert1 = 0
                    likert2 = 0
                    likert3 = 0
                    likert4 = 0
                    likert5 = 0
                    for resp in resp_auto:
                        if resp['id_sprint'] == sprint['id_sprint'] and resp['id_usuario'] == id_usuario and resp['ip'] == str(indice_comp):
                            if resp['resp'] == "1":
                                likert1 += 1
                            elif resp['resp'] == "2":
                                likert2 += 1
                            elif resp['resp'] == "3":
                                likert3 += 1
                            elif resp['resp'] == "4":
                                likert4 += 1
                            elif resp['resp'] == "5":
                                likert5 += 1
                    for resp in resp_grupo:
                        if resp['id_sprint'] == sprint['id_sprint'] and resp['id_usuario_avaliado'] == id_usuario and resp['ip'] == str(indice_comp):
                            if resp['resp'] == "1":
                                likert1 += 1
                            elif resp['resp'] == "2":
                                likert2 += 1
                            elif resp['resp'] == "3":
                                likert3 += 1
                            elif resp['resp'] == "4":
                                likert4 += 1
                            elif resp['resp'] == "5":
                                likert5 += 1

                    coluna = [(likert5), (likert4), (likert3), (likert2), (likert1)]
                    total = sum(coluna)
                    
                    if total != 0:
                        coluna = [(likert5/total)*100, (likert4/total)*100, (likert3/total)*100, (likert2/total)*100, (likert1/total)*100]
                    dados_colunas[sprint['identificacao']] = coluna
                
                indice_comp += 1
                df = pd.DataFrame(dados_colunas, index = ['Excelente', 'Muito bom', 'Bom', 'Razoável', 'Ruim'])
                print(f"\n\033[32;3;1m{comp} (%)\033[m\n")
                print(df.round(2))
                print('\n------------------------------------')
                print("")
            else:
                print('Sem sprints para esse time!')
                break
            
        break