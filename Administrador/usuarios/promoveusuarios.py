import json
import os

caminho_usuarios = "././data/usuarios.json"

def promoveusuarios():
    condicao = True
    while condicao:
            try:
                cpf = input('\033[36;1mDigite o CPF do usuário que será promovido(para cancelar digite 0): \033[m')
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
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("\n\n\033[1;32mUSUÁRIO PROMOVIDO COM SUCESSO\033[m\n")
                            return
                        except:
                            print('\n\033[31mOCORREU ALGUM ERRO!\033[m\n\033[3mTente novamente!\033[m')
                            #print('\n\033[31;1mOcorreu algum erro! Tente novamente\033[m\n')
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    condicao = False
            except ValueError:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('\n\033[31mCPF INVÁLIDO!\033[m\n\033[3mTente novamente!\033[m')
                

    