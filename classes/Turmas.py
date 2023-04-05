#Importando bibliotecas necessárias
import json
import os

#claase que contem os metodos relacionados a turma
class Turmas:
    #variaveis globais
    local_data_turma = ".\\data\\turmas.json"
    

    #método para cadastrar uma turma
    def setDataTurmas(identificacao):

        # busca os dados das turmas ja existentes
        turmas = Turmas.getDataTurmas() 
        
        #calculo do id da turma que será cadastrada
        new_id = int(Turmas.getIdTurma(-1)) + 1
        
        # Cria um dicionário com os dados da turma
        turma = {"id": str(new_id),
                "identificacao": identificacao}
        
        # Adiciona a turma à lista
        turmas.append(turma)
        
        # # Abre o arquivo JSON em modo de escrita
        jls_extract_var = 'w'
        with open(Turmas.local_data_turma,  jls_extract_var) as arquivo:
             # Escreve a lista de usuários no arquivo
             json.dump(turmas, arquivo)
        
        return "Turma Cadastrada!!!"
    
    
    #método para retornar o id da ultima turma cadastrada
    def getIdTurma(posi):
        turmas = Turmas.getDataTurmas()
        ultimaTurma = turmas[posi]
        return ultimaTurma['id']
    
    
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
    
    
    #metodo para printar a identificacao de todas as turmas
    def getAllTurmas():
        x = 1
        for turma in Turmas.getDataTurmas():
            print(x, " - ", turma["identificacao"])
            x = x+1