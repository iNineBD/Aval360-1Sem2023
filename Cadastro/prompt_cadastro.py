import pwinput

from cadastro import cadastro
from senha import criptografar
from cpf import verificacao_cpf
from data import data, data_superior

def prompt_cadastro(data,criptografar):
    # Veridicando se o nome tem caracter especial
    while True:
        nome = input('\nDigite seu nome completo: ').strip()
        nome_testando = nome.replace(" ", "")

        nomes = []

        # Armazenando os caracteres na lista
        for i in nome_testando:
            nomes.append(i)

        if nome_testando.isalpha() == False:
            print("\nNome inválido\n")
        else:
            break

    # Se chegou no CPF significa que o nome está valido
    cpf = input('Digite seu CPF: ').strip()

    while cpf.isnumeric() == False:
        print("\nDigitou um CPF inválido !\n")
        cpf = input('Digite seu CPF: ').strip()

    while len(cpf) != 11 or verificacao_cpf(cpf) == False :

        if len(cpf) < 11:
            print("\nNúmeros insuficientes ou digitou um CPF inválido\n")
            cpf = input('Digite seu CPF: ').strip()
            
        elif len (cpf) > 11:
            print("\nEntrou com mais números que o esperado ou digitou um CPF inválido\n")
            cpf = input('Digite seu CPF: ').strip()
        
        elif verificacao_cpf(cpf) == False:
            print("\nDigitou um CPF inválido\n")
            cpf = input('Digite seu CPF: ').strip()


    data_nascimento = input('Digite a data de nascimento (dd/mm/aaaa) : ')
    data = data(data_nascimento)
    data_superior(data)
    senha = pwinput.pwinput("Digite a senha: ")
    criptografar = criptografar(senha)
    cadastro(nome, cpf,data_nascimento,senha, criptografar)
