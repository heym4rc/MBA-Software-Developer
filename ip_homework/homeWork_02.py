# Programa para Conversão de Moedas

# Solicita ao usuário o valor em reais
print('Conversor de Moedas - Real para Dólar, Euro e Libra Esterlina')
valorReal = float(input('Digite o valor em reais (R$): '))

# Taxas de conversão para diferentes moedas
taxaDolar = 5  # Exemplo de taxa de conversão do real para o dólar
taxaEuro = 6  # Exemplo de taxa de conversão do real para o euro
taxaLibra = 7  # Exemplo de taxa de conversão do real para a libra esterlina

# Calcula o valor convertido para cada moeda
valorDolar = valorReal * taxaDolar
valorEuro = valorReal * taxaEuro
valorLibra = valorReal * taxaLibra

# Exibe os resultados
print(f'Valor em Dólar: ${valorDolar:.2f}')
print(f'Valor em Euro: €{valorEuro:.2f}')
print(f'Valor em Libra Esterlina: £{valorLibra:.2f}')   