import json

caminho_usuario = "././data/usuarios.json"
def excluirusuarios():
    arqv_usuarios = open(caminho_usuario)
    read_arqv_usuarios = json.load(arqv_usuarios)

    print("\nIntegrantes:\n")
       
    indice_vs_usuario_id = {}
    z = 0
    for usuario in read_arqv_usuarios:
        if usuario.get("tp_usu") == 1:
            print(z + 1," - ", usuario.get("identificacao"), end="")
            print(" | CPF:", usuario.get("cpf"))
            indice_vs_usuario_id[str(z)] = usuario.get("id_usuario")
            z += 1

    while True:
        try:
            user_del = int(input("\nEscolha o integrante que deseja excluir: "))
            if user_del > z:
                raise ValueError
            else:
                if user_del == 0:
                     raise  ValueError
                else:
                    break
        except ValueError:
            print("\nValor inválido, tente novamente.")

    userdeletado = read_arqv_usuarios[user_del - 1]
    read_arqv_usuarios.remove(userdeletado)

    with open(caminho_usuario, 'w') as output:
            json.dump(read_arqv_usuarios, output)
    output.close()
    print("\nIntegrante Excluido com Sucesso!!")