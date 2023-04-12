from classes.ctrl_times import Times

def ctrl_times():
    condicao = True
    while condicao:
        print('')
        print("Controle de Times!!!")
        print('')
        print("Escolha uma opção: \n1 - Criar novo time\n2 - Visualizar times\n3 - Editar times\n4 - Excluir times\n5 - Visualizar integrantes\n0 - Voltar\n")
        op = int(input("Digite aqui: "))
        
        if op == 1:
            Times.createTime()
            
        elif op == 2:
            pass
            
        elif op == 3:
            print('\nEdição de Times')
            Times.editTime()
            
        elif op == 4:
            pass
        
        elif op == 5:
            pass
        
        elif op == 0:
            condicao = False
            
        else:
            print('\nOpção inválida! Tente novamente!')
        print("")