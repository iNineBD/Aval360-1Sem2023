import os
import pwinput
from Login.Login import Login
from Cadastro.prompt_cadastro import prompt_cadastro

os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print('')
    print("Sistema de Avaliação 360°")
    print('')
    while True:
        try:
            print("Escolha uma opção: \n1 - Logar\n2 - Cadastrar\n0 - Sair\n")
            op = int(input("Digite aqui: "))
            break
        except ValueError:
            print('\nOpção inválida! Tente novamente!\n')   
        
    if op == 1:
        # Logar
        os.system('cls' if os.name == 'nt' else 'clear')
        cpf = input('Entre com seu CPF: ')
        senha = Login.criptografar_senha(pwinput.pwinput("Digite sua senha: "))
        Login.logar(cpf, senha)
            
    elif op == 2:
        # Cadastrar
        prompt_cadastro()
        
    elif op == 0:
        exit()
            
    else:
        print('\nOpção inválida! Tente novamente!')
    print("----------------------------------------------------")