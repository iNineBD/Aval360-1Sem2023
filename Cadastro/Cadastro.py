import json
import os
import pwinput

from senha import criptografar

#local_usuarios = '.\\data\\usuarios.json'
local_usuarios = 'data/usuarios.json'


def cadastro (nome, cpf, senha,criptografar):

    # Se existir, carrega os usuários existentes
    if os.path.exists(local_usuarios):
            with open(local_usuarios,'r') as arquivo:
                usuarios = json.load(arquivo)
                new_id = int(usuarios[-1]['id_usuario']) + 1
                
    else:
        # Se não existir, cria uma lista vazia
        usuarios = []
        new_id = 0

    for usuario in usuarios:
        if usuario not in usuarios:
            # criando um dicionário com os usuários
            usuario = {'id_usuario': new_id,
                        'nome': nome,
                        'cpf': cpf,
                        'senha': senha,
                        'criptografia': criptografar}
            
            usuarios.append(usuario)
            with open(local_usuarios, 'w') as arquivo:
                 json.dump(usuarios,arquivo)
                 print("\nNovo usuário adicionado com sucesso")
        else:
             print("\nusuário já existe no sistema")
    

#pedindo para digitar os dados de cadastro
nome = input('\nDigite seu nome completo: ')
cpf = input('Digite seu CPF: ')
senha = pwinput.pwinput("Digite a senha: ")
criptografar = criptografar(senha)


cadastro(nome,cpf,senha,criptografar)