import os
import json

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
                turma = json.load(tu)
        else:
            print("As avaliações ainda não começaram! Volte mais tarde!")
            break