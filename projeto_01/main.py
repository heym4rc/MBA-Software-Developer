import time

def listar_herois(lista_herois):
    for heroi in lista_herois:
        print(f'Herói: {heroi[0]}, Identidade Secreta: {heroi[1]}')
        time.sleep(0.800)

def validar_entrada(nome, identidade):
    return nome and identidade

def buscar_heroi(lista_herois, nome):
    for i, heroi in enumerate(lista_herois):
        if heroi[0].lower() == nome.lower():
            return i
    return None

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
        if validar_entrada(nome_heroi, identidade_secreta):
            lista_herois.append([nome_heroi, identidade_secreta])
            print(f'O herói {nome_heroi} foi cadastrado com sucesso!')
        else:
            print("Nome ou identidade secreta inválidos. O cadastro foi cancelado.")
        print() # Linha em branco para melhor visualização
    elif opcao == '2':
        nome_alterar = input("Digite o nome do herói a ser alterado: ")
        encontrado = False
        indice = buscar_heroi(lista_herois, nome_alterar)
        if indice is not None:
            heroi = lista_herois[indice] # Assign heroi here
            novo_nome = input(f"Digite o novo nome para {heroi[0]}: ")
            nova_identidade = input(f"Digite a nova identidade secreta para {heroi[0]}: ")
            if validar_entrada(novo_nome, nova_identidade):
                lista_herois[indice] = [novo_nome, nova_identidade] # Use indice here
                print(f'Herói {heroi[0]} alterado com sucesso para {novo_nome}!')
            else:
                print("Novo nome ou identidade secreta inválidos. A alteração foi cancelada.")
            encontrado = True
            # No break here, as it's not inside a loop
        if not encontrado:
            print(f"Herói '{nome_alterar}' não encontrado na lista.")
        print()  # Linha em branco para melhor visualização
    elif opcao == '3':
        listar_herois(lista_herois)
        time.sleep(1)
        nome_deletar = input("Digite o nome do herói a ser deletado: ")
        encontrado = False
        indice = buscar_heroi(lista_herois, nome_deletar)
        if indice is not None: # This line was missing a colon
                confirmacao = input(f"Tem certeza que deseja deletar {heroi[0]}? (s/n): ").lower()
                if confirmacao == 's':
                    del lista_herois[indice]
                    print(f'Herói {nome_deletar} deletado com sucesso!')
                else:
                    print(f"Exclusão de {nome_deletar} cancelada.")
                encontrado = True
                break
        if not encontrado:
            print(f"Herói '{nome_deletar}' não encontrado na lista.")
        print()  # Linha em branco para melhor visualização
    elif opcao == '4':
        print('--- LISTA DE HERÓIS ---')
        listar_herois(lista_herois)
        time.sleep(1)
        print() # Linha em branco após listar todos os heróis
    else:
        print('Opção inválida. Tente novamente.')
