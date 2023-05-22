import pwinput

from Cadastro.cadastro import cadastro
from Cadastro.senha import criptografar
from Cadastro.cpf import verificacao_cpf
from Cadastro.data import execucao

def prompt_cadastro():
    # Veridicando se o nome tem caracter especial
    while True:
        nome = input('\n\033[36mDigite seu nome completo: \033[m').strip().capitalize()
        nome_testando = nome.replace(" ", "")
        nomes = []
        # Armazenando os caracteres na lista
        for i in nome_testando:
            nomes.append(i)
        if nome_testando.isalpha() == False:
            print("\n\033[31mNOME INVÁLIDO!\033[m\n033[3mTente novamente!\033[m")
        else:
            break

    # Se chegou no CPF significa que o nome está valido
    cpf = input('\033[36mDigite seu CPF: \033[m').strip()
    while cpf.isnumeric() == False:
        print("\n\033[31mCPF INVÁLIDO!\033[m\n\033[3mTente novamente!\033[m")
        cpf = input('\033[36mDigite seu CPF: \033[m').strip()

    while len(cpf) != 11 or verificacao_cpf(cpf) == False :

        if len(cpf) < 11:
            print("\n\033[31mCPF INVÁLIDO!\033[m\n\033[3mVerifique se está correto e Tente novamente!\033[m")
            cpf = input('\033[36mDigite seu CPF: \033[m').strip()
            
        elif len (cpf) > 11:
            print("\n\033[31mCPF INVÁLIDO!\033[m\n\033[3mVerifique se está correto e Tente novamente!\033[m")
            #print("\nEntrou com mais números que o esperado ou digitou um CPF inválido\n")
            cpf = input('\033[36mDigite seu CPF: \033[m').strip()
        
        elif verificacao_cpf(cpf) == False:
            print("\n\033[31mCPF INVÁLIDO!\033[m\n\033[3mVerifique se está correto e Tente novamente!\033[m")
            #print("\nDigitou um CPF inválido\n")
            cpf = input('\033[36mDigite seu CPF: \033[m').strip()


    data_nascimento = execucao()
    senha = criptografar(pwinput.pwinput("\033[36mCadastre uma senha: \033[m"))
    cadastro(nome, cpf,data_nascimento, senha)