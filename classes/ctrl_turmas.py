#Importando bibliotecas necessárias
import json
import os

#claase que contem os metodos relacionados a turma
class Turmas:
    #variaveis globais
    local_data_turma = "data/turmas.json"
    

    #método para cadastrar uma turma
    def createTurmas():
        
        #pede ao usuário a identificacao da nova turma
        identificacao = input("\nEntre com o nome da turma: ")

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
        
        return "Turma Cadastrada!!!"
    
    
    #método para retornar o id da ultima turma cadastrada
    def getNextIdTurma():
        turmas = Turmas.getDataTurmas()
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
            print(f"{x} - {name}")
            x = x+1
        
        
    #metodo para editar uma turma
    def editTurmas():
        #busca os dados de todas as turmas
        turmas = Turmas.getDataTurmas()
        
        #pede ao usuário que entre com a turma que ele deseja editar
        print('\nEscolha uma turma para editar:\n')
        x = 1
        for turma in turmas:
            print(f"{x} - {turma['identificacao']}")
            x=x+1
            
        while True:
            try:
                op = int(input("\nDigite aqui: "))
                if op > x or op == 0:
                    raise ValueError
                break
            except ValueError:
                print('Valor inválido')
        #calcula o index da turma selecionada no dicionário com todas as turmas
        turma_selecionada = turmas[op - 1]
                    
        #salva o id da turma
        id_turma = turma_selecionada['id_turma']
        
        #pede ao usuario a nova identificacao da turma
        new_identificacao = input("\nEntre com a nova identificação: ")
        
        #gera um dicionario com a os dados da turma ja editados
        new_turma = {'id_turma': id_turma,
                     'identificacao': new_identificacao}
        
        #apaga os dados antigos da turma
        del(turmas[op-1])
        
        #concatena os dados editados da turma com os dados de todas as outras turmas
        turmas.append(new_turma)
        
        # salvando os dados no json
        Turmas.setDataTurmas(turmas)
        
        return "Turma editada!!!"
    
    def delTurma():
        #busca os dados de todas as turmas
        turmas = Turmas.getDataTurmas()
        
        #pede ao usuário que entre com a turma que ele deseja excluir
        print('\nEscolha uma turma para excluir:\n')
        x = 1
        for turma in turmas:
            print(f"{x} - {turma['identificacao']}")
            x=x+1
    
        while True:
            try:
                op = int(input("\nDigite aqui: "))
                if op > x or op == 0:
                    raise ValueError
                break
            except ValueError:
                print('Valor inválido')
        #calcula o index da turma selecionada no dicionário com todas as turmas
        turma_selecionada = turmas[op - 1]
        
        #apaga os dados antigos da turma
        del(turmas[op-1])
        
        # salvando os dados no json
        Turmas.setDataTurmas(turmas)
        
        return "Turma excluída!!!"