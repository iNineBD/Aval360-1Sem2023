import pandas as pd 
import json
import os
#Preciso me referir aos json's da auto avaliação e avaliação em grupo

def Dash_global():
    global_autoAvaliacao = open('./data/respostas_autoAvaliacao.json')
    ler_autoAvaliacao = json.load(global_autoAvaliacao)
    global_grupo = open('./data/respostas_grupoAvaliacao.json')
    ler_grupoAvaliacao = json.load(global_grupo)

    
    while True:
        print ('')
        print("Visualização do Indicador Global")
        while True:
            try:
                print("Escolha qual item do Indicador Global deseja gerar: \n1 - Global: Auto Avaliação\n2 - Global Avaliação do grupo\n0 - Voltar")
                op = int(input("Digite aqui: "))
                break 
            except ValueError:
                    print("\nOpção Inválida! Tente Novamente!\n")
            if op == 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    while True:
                        print('')
                        while True:
                            try:
                                print("Escolha qual competência do item de Auto Avaliação deseja gerar: \n1 - Comunicacão e Trabalho em Equipe\n2 - Engajamento e Proatividade\n3 - Conhecimento e Aplicabilidade\n4 - Entrega de Resultados com Valor Agregado\n5 - Autogestão de Atividades\n0 - Voltar")
                                op = int(input("Digite aqui: "))
                                if op == 1:
                                    print('Comunicacão e Trabalho em Equipe')
                                    for ip in ler_autoAvaliacao:
                                        ruim, razoavel, bom, muito_bom, excelente = 0
                                    
                                    if ip == 1:
                                        True: ruim + 1
                                                                                                          
                                    if ip == 2: 
                                        True: razoavel + 1
                                                                            
                                    if ip == 3:
                                        True: bom + 1
                                         
                                    if ip == 4:
                                        True: muito_bom + 1
                                        
                                    if ip == 5:
                                        True: excelente + 10
                                if op == 2:
                                    print('Engajamento e Proatividade')
                                if op == 3:
                                    print('Conhecimento e Aplicabilidade')
                                if op == 4:
                                    print('Entrega de Resultados com Valor Agregado')
                                if op == 5:
                                    print('Autogestão de Atividades')
                                if op == 0:
                                    print('Voltar')                                
                                break
                            except ValueError:
                                    print("\nOpção Inválida! Tente Novamente!\n")
                                    #ip = competência e resposta = escala likert
                            
                                                                
                            if op == 2:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                pass
                        
                            if op == 3:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                pass
                            if op == 4:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                pass
                            if op == 5: 
                                os.system('cls' if os.name == 'nt' else 'clear')
                                pass
                            if op == 0:
                                break
            if op == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                pass 
            while True:
                 print('')
                 while True:
                    try:
                        print("Escolha qual competência do item de Avaliação do Grupo deseja gerar: \n1 - Comunicacão e Trabalho em Equipe\n2 - Engajamento e Proatividade\n3 - Conhecimento e Aplicabilidade\n4 - Entrega de Resultados com Valor Agregado\n5 - Autogestão de Atividades\n0 - Voltar")
                        op = int(input("Digite aqui: "))
                    except ValueError:
                        print("\nOpção Inválida! Tente Novamente!\n")
                    break
        
        return 





            

                    

             



#preciso chamar as perguntas e respostas relacionadas ao grupo (perguntas_grupo_avaliação): 


#preciso computar as respostas relacionadas as competências

#Competência:comunicação e trabalho em equipe
