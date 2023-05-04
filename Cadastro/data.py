from datetime import datetime

def data(data):
    data_str = data
    while ValueError:
        try:
            
            data = datetime.strptime(data_str, '%d/%m/%Y')
            data_formatada = data.strftime("%d/%m/%Y")
            return data_formatada
        except ValueError:
            print('\nDigitou uma data com formatação inválida ou uma data inválida\n')
            data = input('Digite a data de nascimento (dd/mm/aaaa) : ')
            
    
    
def data_superior(data):
    agora = datetime.now()
    agora_formatado = agora.strftime("%d/%m/%Y")
    while datetime.strptime(data, '%d/%m/%Y') > datetime.strptime(agora_formatado, '%d/%m/%Y'):
        print("\nData superior a data atual\n")
        data = input('Digite a data de nascimento (dd/mm/aaaa) : ')
