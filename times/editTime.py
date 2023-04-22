import json

# Função para editar um time
def editTime():
    arqv_turmas = open("./data/turmas.json", encoding="UTF-8")
    ler_arqv_turmas = json.load(arqv_turmas)

    print("\nTurmas:")
    indice_vs_turma_id = {}
    for i in range(len(ler_arqv_turmas)):
        turma = ler_arqv_turmas[i]
        print(i + 1, "-", turma.get("identificacao"))
        indice_vs_turma_id[str(i + 1)] = turma.get("id_turma")

    indice_turma = input("\nDigite o número da turma que deseja visualizar os times: ")
    if indice_turma not in indice_vs_turma_id:
        print("Turma inválida!")
        return

    id_turma = indice_vs_turma_id[indice_turma]

    arqv_times = open("./data/times.json", encoding="UTF-8")
    ler_arqv_times = json.load(arqv_times)

    print("\nTimes:")
    x = False
    indice_vs_time_id = {}
    y = 1
    for i in range(len(ler_arqv_times)):
        time = ler_arqv_times[i]
        if time.get("id_turma") == id_turma:
            print(y, "-", time.get("identificacao"))
            y += 1
            indice_vs_time_id[str(i + 1)] = time.get("id_time")
            x = True

    if not x:
        print("Não há times nesta turma para editar.")
        return

    indice_time = input("\nDigite o número do time que deseja editar: ")
    if indice_time not in indice_vs_time_id:
        print("Time inválido!")
        return

    id_time = indice_vs_time_id[indice_time]
    ind_time_alvo = next((i for i, time in enumerate(ler_arqv_times) if time.get("id_time") == id_time), None)

    if ind_time_alvo is None:
        print("Time não encontrado!")
        return

    print("\nInsira as novas informações:")
    ler_arqv_times[ind_time_alvo]["identificacao"] = input("Nome do time: ")
    ler_arqv_times[ind_time_alvo]["nr_integrantes"] = input("Número máximo de integrantes: ")
    ler_arqv_times[ind_time_alvo]["id_turma"] = id_turma

    print("\n--------------------------")
    print(indice_time, "-", ler_arqv_times[ind_time_alvo]["identificacao"])
    print("--------------------------")
    print("\nEdição realizada com sucesso!")

    with open("./data/times.json", "w", encoding="UTF-8") as f:
        json.dump(ler_arqv_times, f, indent=4)
