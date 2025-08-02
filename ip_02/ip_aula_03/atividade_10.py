# Desafio da Adivinhação!
# O computador pensa um número entre 1 e 100 e o usuário precisa descobrir
# A cada tentativa, o computador dirá se o número é maior ou menor que o palpite

import random
import time

low = 1
high = 100
numero = random.randint(low, high)
palpites = 0

while True:
        palpite = int(input(f"Adivinhe o número entre {low} e {high}: "))
        palpites += 1

        if palpite < low or palpite > high:
            print(f"Por favor, escolha um número entre {low} e {high}.")
        if palpite < numero:
            print("Tente um número maior.")
        elif palpite > numero:
            print("Tente um número menor.")
        else:
            print("Parabéns! Você adivinhou o número!")
            break
        time.sleep(1)  # Pausa de 1 segundo entre as mensagens

print(f"Nesse round os seus palpites foram {palpites}.")

# Fim do desafio