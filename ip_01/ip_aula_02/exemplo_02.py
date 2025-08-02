# Um programa que verifica se existe permissão
# a partir da idade, para entrar em uma festa.

# Solicita a idade do usuário
idade = int(input("Digite a sua idade: "))
ingresso = input("Ingresso VIP ou PISTA: ")

# Verifica a idade e o tipo de ingresso para determinar a permissão de entrada
if idade >= 18 and ingresso == "VIP":
    print("Siga pelo o primeiro andar.")
elif idade >= 18 and ingresso == "PISTA":
    print("Siga pelo corredor.")
else:
    print("É a hora de voltar para sua casa")