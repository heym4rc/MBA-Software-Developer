# Um programa que compara dois números e verifica se são maior ou iguais

# Solicita dois números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Verifica se o primeiro número é maior ou igual ao segundo
if num1 > num2:
    print(f"{num1} é maior {num2}.")
elif num1 < num2:
    print(f"{num1} é menor que {num2}.")
else:
    print(f"{num1} é igual a {num2}.")