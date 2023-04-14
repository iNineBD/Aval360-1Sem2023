import json
#Visualizar Turmas:
arqv_turmas = open('C:/Users/Naiara Lemos/OneDrive/Área de Trabalho/Projeto/turmas.json')
read_arqv_turmas = json.load(arqv_turmas) #load() - leitura do arquivo
print("\nVisualizar Turmas:")
for turma in read_arqv_turmas:
    print(turma.get('id_turma'), "-", turma.get('identificacao'))
num_turmas = str(input('\nDigite qual turma deseja visualizar: '))  #deixar apenas número inteiro

#Visualizar Times:
arqv_times = open('C:/Users/Naiara Lemos/OneDrive/Área de Trabalho/Projeto/times.json')
read_arqv_times = json.load(arqv_times) #load() - leitura do arquivo

print("\nVisualizar Times:")

for time in read_arqv_times:
   if time.get('id_turma') == num_turmas:
        print(time.get('id_time'), '-', time.get('identificacao'))
