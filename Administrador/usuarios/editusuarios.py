import json
from datetime import datetime

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



# Função para editar um time
def editusuarios():
        arqv_turma = open(caminho_turmas, encoding="UTF-8")
        turmas = json.load(arqv_turma)

        arqv_time = open(caminho_times, encoding="UTF-8")
        times = json.load(arqv_time)

        arqv_usuarios = open(caminho_usuarios, encoding="UTF-8")
        usuarios = json.load(arqv_usuarios)
        print("\nTurmas: \n")
        x = 1
        for turma in turmas:
            print(f"{x} - {turma.get('identificacao')}")
            x += 1
            
        while True:
            try:
                entrada_turma = int(input(str("\nDigite qual turma acima deseja visualizar: ")))
                if entrada_turma > x-1:
                    print ("Essa turma não existe")
                else: #
                    turma_escolhida = turmas[entrada_turma - 1]
                    id_turma = turma_escolhida['id_turma']
                    
                    print("\nOpções de time: ")
                    times_pertencentes_turma = []
                    for time in times:  
                        if time.get ('id_turma') == id_turma:
                            times_pertencentes_turma.append(time)
                    y = 1
                    for time in times_pertencentes_turma:
                        print(f"{y} - {time['identificacao']}")
                        y += 1
                    break
            except ValueError:
                print('Valor inválido!')
        while True:
            try:  
                entrada_time = int(input(str("\nDigite qual time deseja visualizar: ")))
                if entrada_time > y-1:
                    print("Time inválido!")
                else:
                    for time in times_pertencentes_turma:
                        if times_pertencentes_turma.index(time) == entrada_time - 1:
                            id_time = time['id_time']
                    break
            except ValueError:
                print('Valor inválido!')
                # print("")
                
        integrantes = []
        for usuario in usuarios:
            if usuario.get ('id_time') == id_time:
                integrantes.append(usuario)
        
        print("\nIntegrantes: \n")

        a = 1
        for integrante in integrantes:
            print(f"{a} - {integrante['identificacao']}")
            a += 1
                
        while True:
            try:  
                entrada_usu = int(input(str("\nEscolha o usuário para editar: ")))
                if entrada_usu > a-1:
                    print("Time inválido!")
                else:
                    id_usu = integrantes[entrada_usu - 1]['id_usuario']
                    integrante_sel = integrantes[entrada_usu - 1]
                    break
            except ValueError:
                print('Valor inválido!')
        
        
        while True:
            nome = input("\nEntre com o nome do usuário: ")
            if valida_nome(nome):
                break
            else:
                print("Nome inválido - Tente novamente!")
        
        while True:
            cpf = input("Entre com o CPF do usuário: ")
            if valida_cpf(cpf):
                break
            else:
                print("CPF inválido - Tente novamente!")
        
        while True:
            data = input('Digite a data de nascimento (dd/mm/aaaa) : ')
            try:
                data = datetime.strptime(data, '%d/%m/%Y')
                if data > datetime.now():
                    print("\nData superior a data atual\n")
                else:
                    data_formatada = data.strftime("%d/%m/%Y")
                    break
            except ValueError:
                print('\nDigitou uma data com formatação inválida ou uma data inválida\n')
            
        for usuario in usuarios:
            if usuario["id_usuario"] == id_usu:
                usuario['identificacao'] = nome
                usuario['dt_nasc'] = data_formatada
                usuario['cpf'] = cpf
                
        
        with open(caminho_usuarios, 'w') as fp:
            json.dump(usuarios, fp)
        fp.close()                