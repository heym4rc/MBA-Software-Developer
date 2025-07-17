# Um programa que calcula o tempo estimado de uma viagem

# Solicita ao usuário a distância da viagem e a velocidade média
distanciaDaViagem = float(input('Qual a distância da viagem em km? '))
velocidadeMedia = float(input('Qual a velocidade média da viagem em km/h? '))

# Calcula o tempo estimado da viagem
print(f'O tempo estimado da viagem é {distanciaDaViagem / velocidadeMedia:.2f} horas.')