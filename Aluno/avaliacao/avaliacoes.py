import json
import os

local_perguntas = '././data/perguntas_autoAvaliacao.json'
local_perguntas_grupo = '././data/perguntas_grupo_avaliacao.json'
local_resposta = '././data/respostas_autoAvaliacao.json'
local_resposta_grupo = '././data/respostas_grupoAvaliacao.json'
local_identificacao = '././data/usuarios.json'

def autoAvaliacao(id_usuario):
    
    print('Autoavaliação:')


    #loop prompt

    # Verifica se o arquivo JSON já existe
    if os.path.exists(local_perguntas):
        # Se existir, carrega as perguntas existentes
        with open(local_perguntas, 'r', encoding="UTF-8") as arquivo:
            perguntas = json.load(arquivo)
    else:
        # Se não existir, cria uma lista vazia
        perguntas = []



    # verifica se o json das respostas ja existe (se alguem ja respondeu ou não)    
    if os.path.exists(local_resposta):
            # abre o arquivo JSON
            with open(local_resposta, 'r', encoding="UTF-8") as resps:
                respostas = json.load(resps)    
    # Lista para armazenar as respostas
    else:
        respostas = []


    # Função para obter a resposta do usuário como um número inteiro entre 1 e 5
    def obter_resposta():
        while True:
            try:
                resposta = int(input("\nPor favor, avalie de 1 a 5: "))
                if resposta < 1 or resposta > 5:
                    raise ValueError
                break
            except ValueError:
                print(
                    "\nNúmero Invalido\nPor favor, insira um número inteiro entre 1 e 5.")
        return resposta


    # função para retornar o maior id das respostas
    def getNextIdResp():
        if os.path.exists(local_resposta):
            # abre o arquivo JSON
            with open(local_resposta, 'r', encoding="UTF-8") as resps:
                respostas = json.load(resps)
            ids = []
            for resposta in respostas:
                ids.append(int(resposta['id_resposta']))
            return max(ids) + 1
        else:
            return 0 
           
    # Loop para obter as respostas do participante
    for pergunta in perguntas:
        print(pergunta["descricao"])
        resposta = {'id_resposta': getNextIdResp(),
                    'ip': str(pergunta["ip"]),
                    'resp': str(obter_resposta()),
                    'id_usuario': id_usuario}
        respostas.append(resposta)  
        # Salvar as respostas em um arquivo JSON
        with open(local_resposta, "w") as arquivo:
            json.dump(respostas, arquivo, indent=5) 
    print("\nRespostas salvas no sistema!.\n")
    y = False
    
def avaliacao(id_usuario, id_time):
            
    # Função para obter a resposta do usuário como um número inteiro entre 1 e 5
    def obter_resposta():
        while True:
            try:
                resposta = int(input("\nPor favor, avalie de 1 a 5: "))
                if resposta < 1 or resposta > 5:
                    raise ValueError
                break
            except ValueError:
                print(
                    "\nNúmero Invalido\nPor favor, insira um número inteiro entre 1 e 5.")
        return resposta


    # função para retornar o maior id das respostas
    def getNextIdResp():
        if os.path.exists(local_resposta_grupo):
            # abre o arquivo JSON
            with open(local_resposta_grupo, 'r', encoding="UTF-8") as resps:
                respostas = json.load(resps)
            ids = []
            for resposta in respostas:
                ids.append(int(resposta['id_resposta']))
            return max(ids) + 1
        else:
            return 0
        
        
    
    time_usuarios = []
    # Verifica se o arquivo JSON já existe
    if os.path.exists(local_identificacao):
        # Se existir, carrega as perguntas existentes
        with open(local_identificacao, 'r', encoding="UTF-8") as usu:
            usuarios = json.load(usu)
    else:
        # Se não existir, cria uma lista vazia
        usuarios = []
    for usuario in usuarios:
        if usuario['id_time'] == id_time and usuario['id_usuario'] != id_usuario:
            time_usuarios.append(usuario)
    
    #para cada usuario pertencente ao time
    for usuario in time_usuarios:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Avaliação do grupo:')
        
        print('\n Em relação a(ao) integrante {}, responda: \n'.format(usuario['identificacao']))
    
        # Verifica se o arquivo JSON já existe
        if os.path.exists(local_perguntas_grupo):
            # Se existir, carrega as perguntas existentes
            with open(local_perguntas_grupo, 'r', encoding="UTF-8") as arquivo:
                perguntas = json.load(arquivo)
        else:
            # Se não existir, cria uma lista vazia
            perguntas = []



        # verifica se o json das respostas ja existe (se alguem ja respondeu ou não)    
        if os.path.exists(local_resposta_grupo):
                # abre o arquivo JSON
                with open(local_resposta_grupo, 'r', encoding="UTF-8") as resps:
                    respostas = json.load(resps)    
        # Lista para armazenar as respostas
        else:
            respostas = []
                    
            
        # Loop para obter as respostas do participante
        for pergunta in perguntas:
            print(pergunta["descricao"])
            resposta = {'id_resposta': getNextIdResp(),
                        'ip': str(pergunta["ip"]),
                        'resp': str(obter_resposta()),
                        'id_usuario_respondeu': id_usuario,
                        'id_usuario_avaliado': usuario['id_usuario']}
            respostas.append(resposta)  
            # Salvar as respostas em um arquivo JSON
            with open(local_resposta_grupo, "w") as arquivo:
                json.dump(respostas, arquivo, indent=5) 
        print("\nRespostas salvas no sistema!.\n")