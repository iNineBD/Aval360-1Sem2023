#Importando bibliotecas necessárias
import json
import os
from time import sleep


#claase que contem os metodos relacionados a turma
class Turmas:
    #variaveis globais
    local_data_turma = "././data/turmas.json"
    local_data_time = "././data/times.json"
    local_data_usu = "././data/usuarios.json"
    local_data_sprint= "././data/sprint.json"
    

    #método para cadastrar uma turma
    def createTurmas():
        
        
        #pede ao usuário a identificacao da nova turma
        identificacao = input("\033[36mDigite o Nome da Turma\033[m: ")

        # busca os dados das turmas ja existentes
        turmas = Turmas.getDataTurmas() 
        
        #calculo do id da turma que será cadastrada
        new_id = Turmas.getNextIdTurma()
        
        # # Cria um dicionário com os dados da turma
        turma = {"id_turma": str(new_id),
                "identificacao": identificacao}
        
        # # Adiciona a turma à lista
        turmas.append(turma)
        
        # salvando os dados no json
        Turmas.setDataTurmas(turmas)

        os.system('cls' if os.name == 'nt' else 'clear')
        return "\n\n\033[1;32mTURMA CRIADA COM SUCESSO\033[m"
          
    #método para retornar o id da ultima turma cadastrada
    def getNextIdTurma():
        turmas = Turmas.getDataTurmas()
        if turmas == []:
            return 0
        else:
            ids = []
            for turma in turmas:
                ids.append(int(turma['id_turma']))
            return max(ids) + 1
    
    
    #método para pegar as informações das demais turmas existentes
    def getDataTurmas():
        # Verifica se o arquivo JSON já existe
        if os.path.exists(Turmas.local_data_turma):
            # Se existir, carrega os usuários existentes
            with open(Turmas.local_data_turma, 'r') as arquivo:
                turmas = json.load(arquivo)
        else:
            # Se não existir, cria uma lista vazia
            turmas = []
        return turmas
    
    
    #salva os dados da turma no json
    def setDataTurmas(turmas):    
        jls_extract_var = 'w'
        with open(Turmas.local_data_turma,  jls_extract_var) as arquivo:
            # Escreve a lista de usuários no arquivo
            json.dump(turmas, arquivo)
        
    
    #metodo para printar a identificacao de todas as turmas
    def getNameAllTurmas():
        name_turmas = []
        for turma in Turmas.getDataTurmas():
            name_turmas.append(turma["identificacao"])
        return name_turmas
    
    
    #metodo para listar todas as turmas
    def listAllTurmas():
        turmas = Turmas.getNameAllTurmas()
        x = 1
        for name in turmas:
            print(f"\033[33;4m{x}\033[m - {name}")
            x = x+1
        
        
    #metodo para editar uma turma
    def editTurmas():
        #busca os dados de todas as turmas
        turmas = Turmas.getDataTurmas()
        
        #pede ao usuário que entre com a turma que ele deseja editar
        #print("\033[36mDigite o Número da Turma que deseja Editar\033[m: ")
        x = 1
        for turma in turmas:
            print(f"\033[33;4m{x}\033[m - {turma['identificacao']}")
            x=x+1
            
        while True:
            try:
                op = int(input("\n\033[36mDigite o Número da Turma que deseja Editar\033[m: "))
                if op > x or op == 0:
                    raise ValueError
                break
            except ValueError:
                print('\n\033[31mOPÇÃO INVÁLIDA!\033[m\n\033[3mTente novamente!\033[m') 
                #print('Valor inválido')
        #calcula o index da turma selecionada no dicionário com todas as turmas
        turma_selecionada = turmas[op - 1]
                    
        #salva o id da turma
        id_turma = turma_selecionada['id_turma']
        
        #pede ao usuario a nova identificacao da turma
        new_identificacao = input("\n\033[36mEscreva o novo nome da Turma: \033[m")
        
        #gera um dicionario com a os dados da turma ja editados
        new_turma = {'id_turma': id_turma,
                     'identificacao': new_identificacao}
        
        #apaga os dados antigos da turma
        del(turmas[op-1])
        
        #concatena os dados editados da turma com os dados de todas as outras turmas
        turmas.append(new_turma)
        
        # salvando os dados no json
        Turmas.setDataTurmas(turmas)
        os.system('cls' if os.name == 'nt' else 'clear')
        return "\n\033[1;32mTURMA EDITADA COM SUCESSO\033[m"
    
    def delTurma():
        #busca os dados de todas as turmas
        turmas = Turmas.getDataTurmas()
        
        #pede ao usuário que entre com a turma que ele deseja excluir
        print('\n\033[36mQual Turma deseja Exluir?:\033[m\n')
        x = 1
        for turma in turmas:
            print(f"\033[33;4m{x}\033[m - {turma['identificacao']}")
            x=x+1
    
        while True:
            try:
                op = int(input("\n\033[36mDigite o Número da Turma que deseja Excluir\033[m: "))
                if op > x or op == 0:
                    raise ValueError
                break
            except ValueError:
                print('\n\033[31mOPÇÃO INVÁLIDA!\033[m\n\033[3mTente novamente!\033[m') 
        #calcula o index da turma selecionada no dicionário com todas as turmas
        turma_selecionada = turmas[op - 1]
        
        #apaga os dados antigos da turma
        del(turmas[op-1])
        
        # salvando os dados no json
        Turmas.setDataTurmas(turmas)
        os.system('cls' if os.name == 'nt' else 'clear')
        return "\n\n\033[1;32mTURMA EXCLUÍDA COM SUCESSO\033[m"
    
    def updateAll(id_turma):
        with open(Turmas.local_data_time) as times:
            times = json.load(times)
        
        with open(Turmas.local_data_sprint) as sprints:
            sprints = json.load(sprints)
        
        with open(Turmas.local_data_usu) as usuarios:
            usuarios = json.load(usuarios)
            
        
        for time in times:
            if time['id_turma'] == id_turma:
                
                id_time = time['id_time']
                
                for usu in usuarios:
                    if usu['id_time'] == id_time:
                        usuarios[usuarios.index(usu)]['id_time'] = ""
                del(times[times.index(time)])
        
        for sprint in sprints:
            if sprint['id_turma'] == id_turma:
                del(sprints[sprints.index(sprint)])
                
        with open(Turmas.local_data_usu, 'w') as usu:
            json.dump(usuarios, usu)
            
        with open(Turmas.local_data_time, 'w') as tim:
            json.dump(times, tim)
            
        with open(Turmas.local_data_sprint, 'w') as spr:
            json.dump(sprints, spr)
