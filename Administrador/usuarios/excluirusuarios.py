import json

caminho_usuario = "././data/usuarios.json"
def excluirusuarios():
    arqv_usuarios = open(caminho_usuario)
    read_arqv_usuarios = json.load(arqv_usuarios)

    print("\n\033[36;1mIntegrantes:\033[m\n")
       
    indice_vs_usuario_id = {}
    z = 1
    for usuario in read_arqv_usuarios:
        if usuario.get("tp_usu") == 1:
            print(f"\033[33;4m{z}\033[m - \033[33;4m{usuario.get('identificacao')}\033[m ",end="")
            print(f" | \033[33;4mCPF:\033[m \033[33;4m{usuario.get('cpf')}\033[m")
            indice_vs_usuario_id[str(z)] = usuario.get("id_usuario")
            z += 1

    while True:
        try:
            user_del = int(input("\n\033[36;1mEscolha o integrante que deseja excluir: \033[m"))
            if user_del > z:
                raise ValueError
            else:
                if user_del == 0:
                     raise  ValueError
                else:
                    break
        except ValueError:
            print("\n\033[31;1mValor inválido, tente novamente.\033[m")

    userdeletado = read_arqv_usuarios[user_del - 1]
    read_arqv_usuarios.remove(userdeletado)

    with open(caminho_usuario, 'w') as output:
            json.dump(read_arqv_usuarios, output)
    output.close()
    print("\n\033[1;32mIntegrante Excluido com Sucesso!!\033[m")