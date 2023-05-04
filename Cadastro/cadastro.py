import json
import os

caminho = os.getcwd()
local_usuarios = os.path.join(caminho, 'data/usuarios.json')

def getNextIdUsuario(usuarios):
        if usuarios == []:
            return 0
        else:
            ids = []
            for usuario in usuarios:
                ids.append(int(usuario['id_usuario']))
            return max(ids) + 1

def cadastro(nome, cpf,data_nascimento, senha, criptografar):

    if os.path.exists(local_usuarios):
        # Carrega os usuários existentes do arquivo
        with open(local_usuarios, 'r') as arquivo:
            usuarios = json.load(arquivo)
    else:
        # Cria uma lista vazia de usuários
        usuarios = []

    # Verifica se o CPF já existe na lista de usuários
    usuario_existente = next((u for u in usuarios if u['cpf'] == cpf), None)

    if usuario_existente is not None:
        print("\nUsuário já existe no sistema\n")
        
    else:
        
        usuario = {
            'id_usuario': getNextIdUsuario(usuarios),
            'identificação': nome,
            'cpf': cpf,
            'senha': criptografar,
            'dt_nasc': data_nascimento,
            'id_time': "",
            'tp_usu': 1}
        
        usuarios.append(usuario)
        
        # Escreve a lista atualizada de usuários no arquivo
        with open(local_usuarios, 'w') as arquivo:
            json.dump(usuarios, arquivo)
            print("\nNovo usuário adicionado com sucesso")