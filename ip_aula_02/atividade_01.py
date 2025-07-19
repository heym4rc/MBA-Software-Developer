# Um programa que verifica se existe permissão
# a partir da idade, para entrar em uma festa.

# Solicita a idade do usuário
idade = int(input("Digite a sua idade: "))
ingresso = input("Ingresso VIP ou PISTA: ")

if idade >= 18 and ingresso == "VIP":
    print("Pode entrar na festa!")
else:
    print("É a hora de voltar para sua casa")