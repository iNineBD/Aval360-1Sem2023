import json

def delTime():
    time_p_del = int(input('Digite o time que deseja excluir: '))

    with open('times.json','w') as json_times:
        ler_arqv_time = json.load(json_times)
        print(ler_arqv_time)

        indice = 0
        for time in ler_arqv_time:
            if time.get('id_time') == time_p_del:
                del(ler_arqv_time[indice])
                break

            indice += 1
        print(ler_arqv_time)

delTime()