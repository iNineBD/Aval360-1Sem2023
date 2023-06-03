import json
import os
competencias = ["Comunicacão e Trabalho em Equipe", "Engajamento e Proatividade", "Conhecimento e Aplicabilidade", "Entrega de Resultados com Valor Agregado", "Autogestão de Atividades"]

def feed_integrante(id_usuario):
        print("\033[32;1mTELA DE FEEDBABCKS\033[m\n")
        if os.path.exists('././data/feedbacks.json'):
          arqv_feed = open('././data/feedbacks.json')
          feed = json.load (arqv_feed)
        else:
               return print('\n\033[31mOPA!\033[m\n\033[3mAinda não há feedbacks!\033[m')


        if os.path.exists('././data/sprint.json'):
          arqv_sprint = open('././data/sprint.json')
          sp = json.load(arqv_sprint)
        else:
               return print('\n\033[31mOPA!\033[m\n\033[3mAinda não há sprints!\033[m')
  
        sprint_integrantes = []
        feedbacks_integrante = []
        competencia = []
        for integrante in feed:
            if integrante['id_usu_avaliado'] == (int(id_usuario)):
                feedbacks_integrante.append(integrante)
                sprint_integrantes.append(integrante['id_sprint'])
                competencia.append(integrante['ip'])
        for sprint in set(sprint_integrantes):
             for x in sp:
                  if x['id_sprint'] == sprint:
                       print(f"\033[36;3mSPRINT:\033[m {x['identificacao']}")
             for comp in competencias:
                  for y in feedbacks_integrante:    
                    if int(y['ip']) == int(competencias.index(comp))+1:
                        print(f'\n\t\033[36;1mCompetência:\033[m {comp}')
                        print(f"\n\t\t\033[36;1;4mFeedback:\033[m \033[3m{y['feedback']}\033[m")