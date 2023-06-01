import json
competencias = ["Comunicacão e Trabalho em Equipe", "Engajamento e Proatividade", "Conhecimento e Aplicabilidade", "Entrega de Resultados com Valor Agregado", "Autogestão de Atividades"]

def feed_integrante(id_usuario):
        arqv_feed = open('././data/feedbacks.json')
        feed = json.load (arqv_feed)

        arqv_sprint = open('././data/sprint.json')
        sp = json.load(arqv_sprint)
  
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
                       print(f"Sprint: {x['identificacao']}")
             for comp in competencias:
                  for y in feedbacks_integrante:    
                    if int(y['ip']) == int(competencias.index(comp))+1:
                        print(f'Competência: {comp}')
                        print(f"\tFeedback: {y['feedback']}")