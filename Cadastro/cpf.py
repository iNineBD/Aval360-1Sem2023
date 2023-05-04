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