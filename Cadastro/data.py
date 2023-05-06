from datetime import datetime

def execucao():
    while True:
        data = input('Digite a data de nascimento (dd/mm/aaaa) : ')
        try:
            data = datetime.strptime(data, '%d/%m/%Y')
            if data > datetime.now():
                print("\nData superior a data atual\n")
            else:
                data_formatada = data.strftime("%d/%m/%Y")
                return data_formatada
        except ValueError:
            print('\nDigitou uma data com formatação inválida ou uma data inválida\n')