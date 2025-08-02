import time

def listar_herois(lista_herois):
    tam_herois = len(lista_herois)
    for i in range(tam_herois):
        print(f'Herói: {lista_herois[i][0]}, Identidade Secreta: {lista_herois[i][1]}')
        time.sleep(0.800)

lista_herois = [
    ['Superman', 'Clark Kent'],
    ['Batman', 'Bruce Wayne'],
    ['Wonder Woman', 'Diana Prince'],
    ['Flash', 'Barry Allen'],
    ['Aquaman', 'Arthur Curry'],
    ['Cyborg', 'Victor Stone'],
    ['Green Lantern', 'Hal Jordan'],
    ['Cyborg', 'Victor Stone'],
    ['Black Widow', 'Natasha Romanoff'],
    ['Spider-Man', 'Peter Parker'],
    ['Iron Man', 'Tony Stark'],
    ['Thor', 'Thor Odinson'],
    ['Hulk', 'Bruce Banner'],
    ['Captain America', 'Steve Rogers'],
    ['Hawkeye', 'Clint Barton'],
    ['Black Panther', 'TChalla'],
]

while True:
    print('### SISTEMA DE SUPER HERÓIS ###')
    print('1 - Cadastrar herói')
    print('2 - Alterar herói')
    print('3 - Deletar herói')
    print('4 - Listar heróis')
    print('0 - Sair do sistema')

    opcao = input('Escolha uma opção: ')
    time.sleep(2)  # Pausa de 2 segundos antes de processar a opção
    print()  # Linha em branco para melhor visualização


    if opcao == '0':
        print('Saindo do sistema...')
        break
    elif opcao == '1':
        # Captura os dados do novo herói
        nome_heroi = input("Digite o nome do herói: ")
        identidade_secreta = input(f"Digite a identidade secreta de {nome_heroi}: ")

        # Valida se os campos não estão vazios antes de adicionar
        if nome_heroi and identidade_secreta:
            lista_herois.append([nome_heroi, identidade_secreta])
            print(f'O herói {nome_heroi} foi cadastrado com sucesso!')
        else:
            print("Nome ou identidade secreta inválidos. O cadastro foi cancelado.")
        print() # Linha em branco para melhor visualização
    elif opcao == '2':
        input("Digite o nome do herói a ser alterado: ")
        time.sleep(1)
        input("Digite o novo nome do herói: ")
        time.sleep(1)
        print('Herói alterado com sucesso!')
        print()  # Linha em branco para melhor visualização
    elif opcao == '3':
        listar_herois(lista_herois)
        time.sleep(1)
        input("Digite o nome do herói a ser deletado: ")
        del lista_herois[-1]
        time.sleep(1)
        print('Herói deletado com sucesso!')
        print()  # Linha em branco para melhor visualização
    elif opcao == '4':
        print('--- LISTA DE HERÓIS ---')
        listar_herois(lista_herois)
        time.sleep(1)
        print() # Linha em branco após listar todos os heróis
    else:
        print('Opção inválida. Tente novamente.')
