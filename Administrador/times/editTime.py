import json

# Função para editar um time
def editTime():
    arqv_turmas = open("././data/turmas.json", encoding="UTF-8")
    ler_arqv_turmas = json.load(arqv_turmas)

    print("\nTurmas:")
    indice_vs_turma_id = {}
    for i in range(len(ler_arqv_turmas)):
        turma = ler_arqv_turmas[i]
        print(f"\n\033[33;4m{i + 1}\033[m - {turma.get('identificacao')}")
        indice_vs_turma_id[str(i + 1)] = turma.get("id_turma")

    indice_turma = input("\n\033[36;1mDigite o número da turma que deseja visualizar os times: \033[m")
    if indice_turma not in indice_vs_turma_id:
        print("\033[31mTurma inválida!\033[m")
        return

    id_turma = indice_vs_turma_id[indice_turma]

    arqv_times = open("././data/times.json", encoding="UTF-8")
    ler_arqv_times = json.load(arqv_times)

    print("\n\033[36;1mTimes:\033[m")
    x = False
    indice_vs_time_id = {}

    y = 1
    for i in range(len(ler_arqv_times)):
        time = ler_arqv_times[i]
        if time.get("id_turma") == id_turma:
            print(f"\033[33;4m{y}\033[m - {time.get('identificacao')}")
            indice_vs_time_id[str(y)] = time.get("id_time")
            y += 1
            x = True

    if not x:
        print("\033[31mNão há times nesta turma para editar.\033[m")
        return

    indice_time = input("\n\033[36;1mDigite o número do time que deseja editar: \033[m")
    if indice_time not in indice_vs_time_id:
        print("\033[31mTime inválido!\033[m")
        return

    id_time = indice_vs_time_id[indice_time]
    ind_time_alvo = next((i for i, time in enumerate(ler_arqv_times) if time.get("id_time") == id_time), None)

    if ind_time_alvo is None:
        print("\033[31mTime não encontrado!\033[m")
        return

    print("\n\033[36;1mInsira as novas informações:\033[m\n")
    ler_arqv_times[ind_time_alvo]["identificacao"] = input("\033[36;1mNome do time: \033[m")
    ler_arqv_times[ind_time_alvo]["nr_integrantes"] = input("\033[36;1mNúmero máximo de integrantes: \033[m")
    ler_arqv_times[ind_time_alvo]["id_turma"] = id_turma

    print("\n\033[33m--------------------------\033[m")
    print(indice_time, "-", ler_arqv_times[ind_time_alvo]["identificacao"])
    print("\033[33m--------------------------\033[m")
    print("\n\033[1;32mEdição realizada com sucesso!\033[m")

    with open("././data/times.json", "w", encoding="UTF-8") as f:
        json.dump(ler_arqv_times, f, indent=4)