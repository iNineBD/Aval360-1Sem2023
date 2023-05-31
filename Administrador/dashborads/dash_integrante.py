import os
import json
import pandas as pd

local_resposta_auto = '././data/respostas_autoAvaliacao.json'
local_resposta_grupo = '././data/respostas_grupoAvaliacao.json'
local_usu = '././data/usuarios.json'
local_sprints = '././data/sprint.json'
local_time = '././data/times.json'
local_turma = '././data/turmas.json'
competencias = ["Comunicacão e Trabalho em Equipe", "Engajamento e Proatividade", "Conhecimento e Aplicabilidade", "Entrega de Resultados com Valor Agregado", "Autogestão de Atividades"]

def dash_integrante_adm():
    while True:
        if os.path.exists(local_resposta_auto) and os.path.exists(local_resposta_grupo):
            with open(local_resposta_auto) as auto:
                resp_auto = json.load(auto)
            with open(local_resposta_grupo) as grupo:
                resp_grupo = json.load(grupo)
            with open(local_sprints) as sp:
                sprints = json.load(sp)
            with open(local_time) as tm:
                times = json.load(tm)
            with open(local_turma) as tu:
                turmas = json.load(tu)
            with open(local_usu) as u:
                usuarios = json.load(u)
        else:
            print("As avaliações ainda não começaram! Volte mais tarde!")
            break
        
        x = 1
        for turma in turmas:
            print(f'{x} - {turma["identificacao"]}')
            x += 1
        print('0 - Voltar')
        
        while True:
            try:
                op_turma = int(input('Escolha uma turma: '))
                if op_turma >= x:
                    raise ValueError
                elif op_turma == 0:
                    return
                else:
                    break
            except:
                print('Opção inválida, tente novamente!')
                
        turma_escolhida = turmas[op_turma-1]
        id_turma = turma_escolhida['id_turma']
        print('')
        
        time_turma = []
        for time in times:
            if time['id_turma'] == turma_escolhida['id_turma']:
                time_turma.append(time)
        
        y = 1
        for time in time_turma:
            print(f"{y} - {time['identificacao']}")
            y+=1
        print('0 - Voltar')
        
        while True:
            try:
                op_time = int(input('Escolha um time: '))
                if op_time >= y:
                    raise ValueError
                elif op_time == 0:
                    return
                else:
                    break
            except:
                print('Opção inválida, tente novamente!')
        
        print('')
        time_escolhido = time_turma[op_time-1]
        
        usu_time = []
        for usu in usuarios:
            if usu['id_time'] == time_escolhido['id_time']:
                usu_time.append(usu)
        
        z = 1
        for usu in usu_time:
            print(f"{z} - {usu['identificacao']} \tCPF: {usu['cpf']}")
            z +=1 
        print('0 - Voltar')
        
        while True:
            try:
                op_usu = int(input('Escolha um usuário: '))
                if op_usu >= z:
                    raise ValueError
                elif op_usu == 0:
                    return
                else:
                    break
            except:
                print('Opção inválida, tente novamente!')
        usu_escolhido = usu_time[op_usu - 1]
        id_usuario = usu_escolhido['id_usuario']



        # pegando as sprints dessa turma
        sprints_turma = []
        for sprint in sprints:
            if int(sprint['id_turma']) == int(id_turma):
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
                print('Sem sprints para esse integrante!')
                break
        break