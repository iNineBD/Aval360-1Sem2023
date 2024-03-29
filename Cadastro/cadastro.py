import json
import os


local_usuarios = './data/usuarios.json'

def getNextIdUsuario(usuarios):
        if usuarios == []:
            return 0
        else:
            ids = []
            for usuario in usuarios:
                ids.append(int(usuario['id_usuario']))
            return max(ids) + 1

def cadastro(nome, cpf,data_nascimento,senha):

    if os.path.exists(local_usuarios):
        # Carrega os usuários existentes do arquivo
        with open(local_usuarios, 'r') as arq:
            usuarios = json.load(arq)
    else:
        # Cria uma lista vazia de usuários
        usuarios = []

    # Verifica se o CPF já existe na lista de usuários
    usuario_existente = next((u for u in usuarios if u['cpf'] == cpf), None)

    if usuario_existente is not None:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n\033[31mUSUÁRIO JÁ CADASTRADO NO SISTEMA!\033[m\n\033[3mTente novamente!\033[m')
        #print("\nUsuário já existe no sistema\n")
        
    else:
        
        usuario = {
            'id_usuario': getNextIdUsuario(usuarios),
            'identificacao': nome,
            'cpf': cpf,
            'senha': senha,
            'dt_nasc': data_nascimento,
            'id_time': "",
            'tp_usu': 1}
        
        usuarios.append(usuario)
        
        # Escreve a lista atualizada de usuários no arquivo
        with open(local_usuarios, 'w') as aq:
            json.dump(usuarios, aq)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n\033[1;32mNOVO USUÁRIO CADASTRADO COM SUCESSO\033[m")
            