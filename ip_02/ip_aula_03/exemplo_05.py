import time
lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

tam_vetor = len(lista[0])

for num in range(tam_vetor):
    print(f'For externo: {lista[num]}')
    time.sleep(1)  # Pausa de 1 segundo entre as impressões

    for num2 in range(len(lista)):
        print(f'For interno: {lista[num][num2]}')
        time.sleep(1)  # Pausa de 1 segundo entre as impressões