import json

caminho_usuarios = "././data/usuarios.json"

def promoveusuarios():
    condicao = True
    while condicao:
        while True:
            try:
                cpf = input('Digite o CPF do usuário que será promovido: (para cancelar digite 0) ')
                if cpf != "0":
                    with open(caminho_usuarios, 'r') as usu:
                        usuarios = json.load(usu)
                    
                    for usuario in usuarios:
                        if usuario['cpf'] == cpf:
                            usuario_ok = usuario
                            indice = usuarios.index(usuario_ok)
                            break
                    
                    if "usuario_ok" not in locals():
                        raise ValueError
                    else:
                        try:
                            usu_prom = {
                                "id_usuario": usuario_ok['id_usuario'],
                                "identificacao": usuario_ok['identificacao'],
                                "senha": usuario_ok['senha'],
                                "cpf": usuario_ok['cpf'],
                                "tp_usu": 0,
                                "dt_nasc": usuario_ok['dt_nasc'],
                                "id_time": 10000
                            }
                            
                            del(usuarios[indice])
                            
                            usuarios.append(usu_prom)
                            
                            with open(caminho_usuarios, 'w') as usus:
                                json.dump(usuarios, usus)
                            
                            print('Usuário promovido com sucesso!!!')
                            return
                        except:
                            print('Ocorreu algum erro! Tente novamente')
                else:
                    break
            except ValueError:
                print('CPF inválido.')

    