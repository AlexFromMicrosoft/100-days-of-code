import random

# Rock
pedra = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
papel = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
tesoura = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

jokempo = [pedra, papel, tesoura]
entrada = input("Qual será sua escolha? Digite 0 para Pedra, 1 para Papel, 2 para Tesoura:\n")
cpu = random.choice(jokempo)
user_i = int(entrada)

# Caso Digite Algo Maior que 20
if user_i >= 3:
    print("Valor inválido! Tente novamente...")

# PEDRA
if user_i == 0:
    print(f"Você escolheu\n{jokempo[0]}\n")
    if cpu == pedra:
        print(f"Computador escolheu\n{jokempo[0]}")
        print("Empate")
    if cpu == papel:
        print(f"Computador escolheu\n{jokempo[1]}")
        print("Derrota")
    if cpu == tesoura:
        print(f"Computador escolheu\n{jokempo[2]}")
        print("Vitória")
#PAPEL
if user_i == 1:
    print(f"Você escolheu\n{jokempo[1]}\n")
    if cpu == pedra:
        print(f"Computador escolheu\n{jokempo[0]}")
        print("Vitória")
    if cpu == papel:
        print(f"Computador escolheu\n{jokempo[1]}")
        print("Empate")
    if cpu == tesoura:
        print(f"Computador escolheu\n{jokempo[2]}")
        print("Derrota")
#TESOURA
if user_i == 2:
    print(f"Você escolheu\n{jokempo[2]}\n")
    if cpu == pedra:
        print(f"Computador escolheu\n{jokempo[0]}")
        print("Derrota")
    if cpu == papel:
        print(f"Computador escolheu\n{jokempo[1]}")
        print("Vitória")
    if cpu == tesoura:
        print(f"Computador escolheu\n{jokempo[2]}")
        print("Empate")
