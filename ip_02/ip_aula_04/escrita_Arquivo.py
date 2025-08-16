from datetime import datetime

data = datetime.now().strftime('%Y%m%d_%H%M')

with open(f'ling_prog_{data}.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Eu amo programar\n')
    arquivo.write('Eu amo ganhar dinheiro\n')
    arquivo.write('Eu amo estudar\n')