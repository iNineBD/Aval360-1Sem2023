import json
import os
import hashlib
from Administrador.prompt_main_adm import promptMainAdm
from Aluno.promptAvaliacao import prompt_avaliacao

caminho_usuarios = "./data/usuarios.json"
caminho_times = "./data/times.json"

class Login:
    
    #funcao para logar
    def logar(cpf, senha):
        
        #abre o arquivo json dos usuarios
        with open(caminho_usuarios, 'r', encoding="UTF-8") as usuarios:
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
                    
                elif usu_ok['tp_usu'] == 1 and type(usu_ok["id_time"]) is int:
                    prompt_avaliacao(usu_ok['id_usuario'])
                    
                elif usu_ok['tp_usu'] == 1 and type(usu_ok["id_time"]) is str:
                    index_usuario = usuarios.index(usu_ok)
                    Login.setTimeUsu(usu_ok['id_usuario'], index_usuario)
                    
                    prompt_avaliacao(usu_ok["id_usuario"])
                    
                    
            else:
                # se n estiver ok, erro
                raise ValueError
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n\033[31mCREDENCIAIS INVÁLIDAS!\n\033[m\033[3mTente novamente!\033[m') 
            
            
    def setTimeUsu(id_usu, index_usu):
        while True:
            try:
                cod =  input('\033[36;3mDigite o Código de Acesso: \033[m')
                if not Login.verificaCod(cod):
                    raise ValueError
                else:
                    id_time = Login.verificaCod(cod)
                    break
            except:
                print('\n\033[31mCÓDIGO DE ACESSO INVÁLIDO!\n\033[m\033[3mTente novamente!\033[m') 
        
        with open(caminho_usuarios, encoding="UTF-8") as usuarios:
            usuarios = json.load(usuarios)
        
        usuario = usuarios[index_usu]
        
        new_usu = {
            "id_usuario": usuario["id_usuario"],
            "identificacao": usuario["identificacao"],
            "senha": usuario["senha"],
            "cpf": usuario["cpf"],
            "tp_usu": 1,
            "dt_nasc": usuario["dt_nasc"],
            "id_time": id_time
            }
        
        del(usuarios[index_usu])
        
        usuarios.append(new_usu)
        
        with open(caminho_usuarios, 'w') as usu:
            json.dump(usuarios, usu)
            
        
    def verificaCod(cod):
        with open(caminho_times) as times:
            times = json.load(times)
        
        for time in times:
            if time["cod_acesso"] == cod:
                id_time = time['id_time']
                break
        if "id_time" in locals():
            return id_time
        else:
            return False
        
            
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