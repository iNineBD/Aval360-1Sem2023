from classes.ctrl_turmas import Turmas

while True:
    print('')
    print("Controle de Turmas!!!")
    print('')
    print("Escolha uma opção: \n1 - Criar nova turma\n2 - Visualizar turmas\n3 - Editar turma\n4 - Controle de times\n0 - Voltar\n")
    op = int(input("Digite aqui: "))
    if op == 1:
        ident = input("\nEntre com o nome da turma: ")
        print(Turmas.createTurmas(ident))
    elif op == 2:
        turmas = Turmas.getNameAllTurmas()
        x = 1
        for name in turmas:
            print(f"{x} - {name}")
            x = x+1
    elif op == 3:
        pass
    elif op == 4:
        pass
    elif op == 0:
        exit()
    else:
        print('\nOpção inválida! Tente novamente!')
    print("----------------------------------------------------")