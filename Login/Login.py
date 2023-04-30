import json
import os
import hashlib
from Administrador.prompt_main_adm import promptMainAdm
from Aluno.promptAvaliacao import prompt_avaliacao

caminho_usuarioa = "./data/usuarios.json"

class Login:
    
    #funcao para logar
    def logar(cpf, senha):
        
        #abre o arquivo json dos usuarios
        with open(caminho_usuarioa, 'r') as usuarios:
            usuarios = json.load(usuarios)
        
        for usuario in usuarios:
            # verifica se senha e cpf estão ok
            if usuario['senha'] == senha and usuario['cpf'] == cpf:
                usu_ok = usuario
                break
        
        try:
            # se estiver ok, o programa verifica se é adm ou aluno
            if "usu_ok" in locals():
                if usu_ok['tp_usu'] == 0:
                    promptMainAdm()
                    
                elif usu_ok['tp_usu'] == 1:
                    prompt_avaliacao(usu_ok['id_usuario'])
                    
            else:
                # se n estiver ok, erro
                raise ValueError
        except ValueError:
            print('Credenciais inválidas!!! Tente novamente.')
            
    def criptografar_senha(senha):
        # Cria um objeto de hash usando o algoritmo SHA-256
        hash_object = hashlib.sha256()
        # Codifica a senha em bytes antes de passá-la para a função hash
        senha_codificada = senha.encode('utf-8')
        # Atualiza o objeto de hash com a senha codificada
        hash_object.update(senha_codificada)
        # Obtém a representação hexadecimal do valor de hash
        senha_criptografada = hash_object.hexdigest()
        # Retorna a senha criptografada
        return senha_criptografada