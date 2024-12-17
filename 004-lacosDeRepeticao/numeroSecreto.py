#Jogo do Número Secreto

import random

numeroSecreto = random.randint(1, 10)
chute = 0

print("Bem-vindo ao jogo do Número Secreto!")
print("Adivinhe o número que estou pensando entre 1 e 10.")

while chute != numeroSecreto:
    chute = int(input("Seu chute: "))
    if chute < numeroSecreto:
        print("Muito abaixo, tente novamente")
    elif chute > numeroSecreto:
        print("Muito acima, tente novamente")
    else:
        print("Parabéns, vocé acertou!")    

print("Fim do jogo")

print("\n")
