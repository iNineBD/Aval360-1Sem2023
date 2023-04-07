from classes.ctrl_turmas import Turmas

while True:
    print('')
    print("Controle de Turmas!!!")
    print('')
    print("Escolha uma opção: \n1 - Criar nova turma\n2 - Visualizar turmas\n3 - Editar turma\n4 - Controle de times\n0 - Voltar\n")
    op = int(input("Digite aqui: "))
    
    if op == 1:
        print("\nCriar nova turma!!!\n")
        print(Turmas.createTurmas())
        
    elif op == 2:
        print("\nVisualizando turmas!!!\n")
        Turmas.listAllTurmas()
        
    elif op == 3:
        print("\nEditar turma!!!\n")
        print(Turmas.editTurmas())
        
    elif op == 4:
        pass
    elif op == 0:
        exit()
    else:
        print('\nOpção inválida! Tente novamente!')
    print("----------------------------------------------------")