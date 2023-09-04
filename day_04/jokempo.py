from art import pedra
from art import papel
from art import tesoura

import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print('-'*40)
print(f'{" "*15}Jokempo'.upper())
print('-'*40)
jokempo = [pedra, papel, tesoura]
jogador = int(input("Jokempo escolha:\nPedra[1], Papel[2], Tesoura[3]: "))
banca = random.choice(jokempo)
print('-'*40)
print(f"{' '*15}A banca joga".upper())
print('-'*40)
print(banca)

if jogador == 1:
    escolha = jokempo[0]
    print('-'*40)
    print(f"{' '*15}você joga".upper())
    print('-'*40)
    print(escolha)
    if banca == jokempo[1]:
        print('Derrota') 
    elif banca == jokempo[2]:
        print("Vitória")
if jogador == 2:
    escolha = jokempo[1]
    print('-'*40)
    print(f"{' '*15}você joga".upper())
    print('-'*40)
    print(escolha)
    if banca == jokempo[2]:
        print('Derrota') 
    elif banca == jokempo[0]:
        print("Vitória")
if jogador == 3:
    escolha = jokempo[2]
    print('-'*40)
    print(f"{' '*15}você joga".upper())
    print('-'*40)
    print(escolha)
    if banca == jokempo[0]:
        print('Derrota') 
    elif banca == jokempo[1]:
        print("Vitória")

if escolha == banca:
    print('Empate')

print('-'*40)

saida = input('Aperte ENTER para Limpar a tela')
if saida != 'ajkdasjdnasdjklsna':
    clear()



