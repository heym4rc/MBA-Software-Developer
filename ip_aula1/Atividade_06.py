PI = 3.14
altura = float(input('Digite o valor da altura:'))
raio = float(input('Digite o valor do raio:'))

lateral = 2 * PI * raio * altura 
base = PI * (raio ** 2)
area_cilindro = base + lateral

quantidade_total = area_cilindro / 3
quantidade = quantidade_total / 5
custo = 50 * quantidade

print(f'O custo total da pintura é R${custo: .2f}')