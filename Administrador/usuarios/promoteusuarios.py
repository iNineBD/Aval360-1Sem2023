import json

caminho_usuarios = "././data/usuarios.json"

def verificacao_cpf(cpf):
    def vd_1(cpf):

        digitos=[]
        # armazenando os dígitos na lista
        for numero_cpf in cpf:
            if len(digitos) <= 11:
                digitos.append(numero_cpf)

        x = 10 
        soma = 0

        # pegando os primeiros 9 dígitos da lista
        for digito in digitos[0:9]:
            if len(digito) < 9:
                soma += (int(digito) * x)
                x -=1

        digito = soma % 11

        dv_1 = False

        # Quando o digito é maior ou igual a 2
        if digito >= 2:
            if int(11-digito) == int(digitos[9]):
                dv_1 = True

        # Quando o dígito é menor que 2
        elif digito < 2:
            digito = 0
            if int(digito) == int(digitos[9]):
                dv_1 = True
        
        return dv_1

    def vd_2 (cpf):
        
        digitos=[]
        # armazenando os dígitos na lista
        for numero_cpf in cpf:
            if len(digitos) <= 11:
                digitos.append(numero_cpf)
        
        x = 11 
        soma = 0

        # pegando os primeiros 9 dígitos da lista
        for digito in digitos[0:10]:
            if len(digito) < 9:
                soma += (int(digito) * x)
                x -=1

        digito = soma % 11

        dv_2 = False

        # Quando o digito é maior ou igual a 2
        if digito >= 2:
            if int(11-digito) == int(digitos[10]):
                dv_2 = True

        # Quando o dígito é menor que 2
        elif digito < 2:
            digito = 0
            if int(digito) == int(digitos[10]):
                dv_2 = True
        
        return dv_2

    digito_1 = vd_1(cpf)
    digito_2 = vd_2(cpf)

    if digito_1 == True and digito_2 == True:

        return True
    
    else:
        return False



def promoteusuarios():
    while True:
        try:
            cpf = input('Digite o CPF do usuário que será promovido: ')
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
                break
        except ValueError:
            print('CPF inválido.')
        
    while True:
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
            break
        except:
            print('Ocorreu algum erro! Tente novamente')
    