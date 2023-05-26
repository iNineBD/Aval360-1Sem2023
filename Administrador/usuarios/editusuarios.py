import json
from datetime import datetime
import os

caminho_turmas = "././data/turmas.json"
caminho_times = "././data/times.json"
caminho_usuarios = "././data/usuarios.json"

def valida_cpf(cpf):
    # remove caracteres não numéricos do CPF
    cpf = ''.join(filter(str.isdigit, cpf))

    # verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # calcula o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto

    # calcula o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto

    # verifica se os dígitos verificadores são iguais aos do CPF
    if cpf[-2:] == str(digito1) + str(digito2):
        return True
    else:
        return False
    
    
def valida_nome(nome):
    if nome.isalpha() or nome.replace(' ', '').isalpha():
        return True
    else:
        return False

def cpf_repetido(cpf):
    with open(caminho_usuarios) as usu:
        usu = json.load(usu)
    
    for i in usu:
        if i['cpf'] == cpf:
            return False
    
    return True



# Função para editar um time
def editusuarios():
        arqv_turma = open(caminho_turmas, encoding="UTF-8")
        turmas = json.load(arqv_turma)

        arqv_time = open(caminho_times, encoding="UTF-8")
        times = json.load(arqv_time)

        arqv_usuarios = open(caminho_usuarios, encoding="UTF-8")
        usuarios = json.load(arqv_usuarios)
        print("\033[36;1mTurmas: \033[m\n")
        x = 1
        for turma in turmas:
            print(f"\033[33;4m{x}\033[m - {turma.get('identificacao')}")
            x += 1
            
        while True:
            try:
                print("\033[33;4m0\033[m - Voltar")
                entrada_turma = int(input(str("\n\033[36;1mDigite qual turma acima deseja visualizar: \033[m")))
                if entrada_turma > x-1:
                    print ("\033[31mEssa Turma Não Existe!\033[m\n\033[31mTente Novamente!\033[m")
                elif entrada_turma == 0:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return
                else: 
                    turma_escolhida = turmas[entrada_turma - 1]
                    id_turma = turma_escolhida['id_turma']
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("\n\033[36;1mOpções de time: \033[m\n")
                    times_pertencentes_turma = []
                    for time in times:  
                        if time.get ('id_turma') == id_turma:
                            times_pertencentes_turma.append(time)
                    y = 1
                    for time in times_pertencentes_turma:
                        print(f"\033[33;4m{y}\033[m - {time['identificacao']}")
                        y += 1
                    break
            except ValueError:
                print('\033[1;31mValor inválido!\033[m')
        while True:
            try:
                print("\033[33;4m0\033[m - Voltar")  
                entrada_time = int(input(str("\n\033[36;1mDigite qual time deseja visualizar: \033[m")))
                if entrada_time > y-1:
                    print("\033[1;31mTime inválido!\033[m")
                elif entrada_time == 0:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return
                else:
                    for time in times_pertencentes_turma:
                        if times_pertencentes_turma.index(time) == entrada_time - 1:
                            id_time = time['id_time']
                    break
            except ValueError:
                print('\033[1;31mValor inválido!\033[m')
                # print("")
                
        integrantes = []
        for usuario in usuarios:
            if usuario.get ('id_time') == id_time:
                integrantes.append(usuario)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n\033[36;1mIntegrantes: \033[m\n")

        a = 1
        for integrante in integrantes:
            print(f"\033[33;4m{a}\033[m - {integrante['identificacao']}")
            a += 1
                
        while True:
            try:
                print("\033[33;4m0\033[m - Voltar")
                entrada_usu = int(input(str("\n\033[36;1mEscolha o usuário para editar: \033[m")))
                if entrada_usu > a-1:
                    print("\033[31;1mTime inválido!\033[m")
                elif entrada_usu == 0:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return
                else:
                    id_usu = integrantes[entrada_usu - 1]['id_usuario']
                    integrante_sel = integrantes[entrada_usu - 1]
                    break
            except ValueError:
                print('\033[31;1mValor inválido!\033[m')
        
        
        while True:
            nome = input("\n\033[36;1mEntre com o nome do usuário: \033[m")
            if valida_nome(nome):
                break
            else:
                print("\033[36;1mNome inválido - Tente novamente!\033[m")
        
        while True:
            cpf = input("\033[36;1mEntre com o CPF do usuário: \033[m")
            if valida_cpf(cpf) and cpf_repetido(cpf):
                break
            else:
                print("\033[31;1mCPF inválido - Tente novamente!\033[m")
        
        while True:
            data = input('\033[36;1mDigite a data de nascimento (dd/mm/aaaa) : \033[m')
            try:
                data = datetime.strptime(data, '%d/%m/%Y')
                if data > datetime.now():
                    print("\n\033[31;1mData superior a data atual\033[m\n")
                else:
                    data_formatada = data.strftime("%d/%m/%Y")
                    break
            except ValueError:
                print('\n\033[31;1mDigitou uma data com formatação inválida ou uma data inválida\033[m\n')
            
        for usuario in usuarios:
            if usuario["id_usuario"] == id_usu:
                usuario['identificacao'] = nome
                usuario['dt_nasc'] = data_formatada
                usuario['cpf'] = cpf
                
        
        with open(caminho_usuarios, 'w') as fp:
            json.dump(usuarios, fp)
        fp.close()
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n\033[1;32mIntegrante Editado com Sucesso!!\033[m")                