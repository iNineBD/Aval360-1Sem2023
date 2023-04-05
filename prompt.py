from classes.Turmas import Turmas

while True:
    print('')
    print("Controle de Turmas!!!")
    print('')
    print("Escolha uma opção: \n1 - Criar nova turma\n2 - Visualizar turmas\n3 - Voltar\n")
    op = int(input("Digite aqui: "))
    if op == 1:
        ident = input("\nEntre com a identificação da turma: ")
        print(Turmas.setDataTurmas(ident))
    elif op == 2:
        Turmas.getAllTurmas()
    elif op == 3:
        exit()
    else:
        print('Opção inválida! Tente novamente!')
    print("----------------------------------------------------")
    
    #AINDA FALTA A OPÇÃO DE EDITAR TURMAS (E TODA A PARTE DOS TIMES)
    #PROPOR MUDANÇA NO FLUXOGRAMA (NAVEGABILIDADE - FAZER UM MENU COM TODAS AS POSSÍVEIS OPÇÕES)