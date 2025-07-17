# Programa para Calcular o Volume de uma Esfera

PI = 3.1415 # Valor aproximado de PI
# Solicita ao usuário o raio da esfera
raio = float(input('Digite o raio da esfera: '))

# Calcula o volume da esfera usando a fórmula V = (4/3) * π * r³
volume = (4/3) * PI * (raio ** 3)

# Exibe o resultado
print(f'O volume da esfera com raio {raio} é: {volume:.2f}')  # Exibe o resultado formatado com duas casas decimais