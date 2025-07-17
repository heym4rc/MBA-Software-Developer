# Um programa que verifica se um número é par ou ímpar
while True: # while True para repetir o processo até que o usuário decida sair
    # Solicita ao usuário se deseja verificar um número ou não
    usuario = input('Você deseja verificar se um número é par ou ímpar? (s/n): ').strip().lower()
    if usuario in ('n', 'não'): # Se o usuário não quiser continuar, encerra o programa
        print('Até a próxima.')
        break 
    
    # Solicita um número ao usuário e verifica se é par ou ímpar
    try:
        numero = int(input('Digite um número: '))
    # Se o usuário inserir um valor inválido, exibe uma mensagem de erro
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

    # Verifica se o número é par ou ímpar
    if numero % 2 == 0:
        print(f'O número {numero} é par')
    else:
        print(f'O número {numero} é ímpar')

    print('---' * 10)  # Exibe uma linha de separação para melhor visualização