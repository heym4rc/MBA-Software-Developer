# Programa que converte temperatura entre Celsius e Fahrenheit

# Solicita a temperatura e a escala
temperatura_str = input("Digite a temperatura (ex: 25C ou 77F): ")
temperatura = float(temperatura_str[:-1])
escala = temperatura_str[-1].upper()

# Converte a temperatura e exibe o resultado
if escala == 'C':
    temperatura_convertida = (temperatura * 9/5) + 32
    print(f"{temperatura}°C é igual a {temperatura_convertida:.2f}°F.")
elif escala == 'F':
    temperatura_convertida = (temperatura - 32) * 5/9
    print(f"{temperatura}°F é igual a {temperatura_convertida:.2f}°C.")
else:
    print("Escala inválida. Use 'C' para Celsius ou 'F' para Fahrenheit.")