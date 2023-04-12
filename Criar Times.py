import json

arquivo_das_turmas = open("C:/Users/jaque/OneDrive/Documentos/Teste GitHub/opa/Teste-Jaque/turmas.json")
turmas= json.load (arquivo_das_turmas)
arquivo_times = open("C:/Users/jaque/OneDrive/Documentos/Teste GitHub/opa/Teste-Jaque/times.json")
times= json.load (arquivo_times)

print('\nTurmas')

for turma in turmas:
    print(turma['id_turma'], '-', turma['identificacao'])

op = int(input("Selecione uma turma: "))

Identificacao_time = input(" Entre com a identificacao do time: ")
numero_max_integrantes = input (" Entre com o numero maximo de pessoas no time: ")

maior_id_time = 0
for time in times:
    if maior_id_time < time['id']:
        maior_id_time = time['id']

novo_time = {
    'id': maior_id_time + 1,
    'identificacao': Identificacao_time,
    'nr_integrantes': numero_max_integrantes,
    'id_turma': op
}
times.append(novo_time)

with open('C:/Users/jaque/OneDrive/Documentos/Teste GitHub/opa/Teste-Jaque/times.json', 'w') as f:
    # Escrevendo os dados atualizados no arquivo
    json.dump(times, f)

    print('Time criado!')

exit()



salvando_arquivo_json = "C:/Users/jaque/OneDrive/Documentos/Teste GitHub/opa/Teste-Jaque/times.json"

with open(salvando_arquivo_json, 'w') as output:
    json.dump (leitura_do_arquivo, output)
output.close()
