from datetime import datetime

def execucao():
    while True:
        data = input('\033[36mDIGITE A DATA DE NASCIMENTO (dd/mm/aaaa) : \033[m')
        try:
            data = datetime.strptime(data, '%d/%m/%Y')
            if data > datetime.now():
                print("\n\033[31;3mATENÇÃO!\nData deve ser superior a data atual\033[m")
            else:
                data_formatada = data.strftime("%d/%m/%Y")
                return data_formatada
        except ValueError:
            print('\n\033[31mFORMATO OU DATA INVÁLIDA...\033[m\n\033[3mTente novamente!\033[m')            
            #print('\nDigitou uma data com formatação inválida ou uma data inválida\n')