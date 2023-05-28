import os
# from Aluno.dashboards.dashs_time import dashs_time
from dashs_time import dashs_time

def ctrl_dashs(id_usuario, id_time):
    print("\033[32;1mVISUALIZAÇÃO DE DASHBOARDS\033[m\n")
    while True:
        while True:
            try:
                print("\033[36;1m\nESCOLHA UMA OPÇÃO:\n\033[m \n\033[33;4m1\033[m - Seu time\n\033[33;4m2\033[m - Você\n\033[33;4m0\033[m - Voltar\n")
                #print("\033[3mCerto, escolha uma opção\033[m:\n\n1 - Criar Turma\n2 - Visualizar Turma\n3 - Editar Turma\n4 - Excluir Turma\n0 - Voltar\n")
                op = int(input("\033[36;1mO QUE DESEJA FAZER?: \033[m"))
                #op = int(input("\033[3;33;1mDigite aqui\033[m: "))
                break
            except ValueError:
                print('\n\033[31mOPÇÃO INVÁLIDA!\033[m\n\033[3mTente novamente!\033[m')
                #print('\n\033[1;31mOPÇÃO INVÁLIDA!\nTente novamente...\033[m\n')
        
        if op == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n\033[3;1mVocê escolheu a opção:\033[m \033[33m"Seu time"\033[m\n')
            dashs_time(id_usuario, id_time)
                    
        elif op == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n\033[3;1mVocê escolheu a opção:\033[m \033[33m"Você"\033[m\n')
            pass
        
        elif op == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            break
            
        else:
            print('\n\033[31mOPÇÃO INVÁLIDA!\033[m\n\033[3mTente novamente!\033[m')

ctrl_dashs(0, 1)