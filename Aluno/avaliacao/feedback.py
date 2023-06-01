import json
import os

caminho_feedbacks = '././data/feedbacks.json'

def nextId():
    if os.path.exists(caminho_feedbacks):
        with open(caminho_feedbacks) as feedbacks:
            feedbacks = json.load(feedbacks)
        ids = []
        for i in feedbacks:
            ids.append(i['id_feedback'])
        return max(ids) + 1
    else:
        return 0

def setFeedback(id_usu_avaliador, id_usu_avaliado, id_sprint, id_resp, id_pergunta):
    while True:
        try:
            feedback = input("\n\033[33mExplique o motivo da nota: \033[m")
            if feedback == "":
                raise ValueError
            else:
                break
        except ValueError:
            print("O feedback é obrigatório!")
    
    if os.path.exists(caminho_feedbacks):
        with open(caminho_feedbacks, 'r') as feedbacks:
            feedbacks = json.load(feedbacks)
    else:
        feedbacks = []
    
    novo_feed = {
        'id_feedback': nextId(),
        'id_usu_avaliador': id_usu_avaliador,
        'id_usu_avaliado': id_usu_avaliado,
        'id_resposta': id_resp,
        'id_sprint': id_sprint,
        'ip': id_pergunta,
        'feedback': feedback
    }
    
    feedbacks.append(novo_feed)
    
    with open(caminho_feedbacks, 'w') as fp:
        json.dump(feedbacks, fp)
        
    print('')