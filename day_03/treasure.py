import random
from dados import dado
from clear import clear

clear()
d20 = random.choice(dado)

print("bem vindo a caça ao tesouro! Seu objetivo é encontrar o tesouro da ilha".title())
print("\nSempre que se deparar com um perigo role um dado.")

estrada = input("\nDurante sua viagem pela estrada você se depara com uma bifurcação, o que você faz?\nDigite [Esquerda] ou [Direita]: ").lower()
clear()

# Pela esquerda
if estrada == 'esquerda':
    lago = input(f'\nVocê segue seu caminho a {estrada}. Logo encontra um lago e avista a tão falada ilha. Para chegar na ilha você prefere ir de barco ou ir nadando?\nDigite: [Nadar] ou [Barco]: ')
    clear()
    
    # Pelo Barco
    if lago == "barco":
        ilha = input("\nCom segurança você chega a ilha. Caminhando um pouco encontra a masmorra, Dentro da masmorra existem três portas, qual você escolhe?\nDigite [Vermelha], [Azul] ou [Amarela]: ").lower()
        clear()
        
        # Porta vermelha
        if ilha == 'vermelha':
            print("Oh Não! Uma armadilha de chamas...")
            print("GAME OVER!")
        
        # Porta azul
        elif ilha == 'azul':
            d20 = random.choice(dado)
            if d20 >= 10:
                print(f"Dado = {d20}")
                print("Monstros te atacam! Em um ambiente fechado é uma luta difícil de alguma forma você da\num jeito.")
                chance = input("Escolha outra porta:\nDigite [Vermelha] ou [Amarela]: ").lower()
                clear()
                if chance == 'amarela':
                    print('Você encontrou o tesouro!!!')
                    print('GAME OVER!')
                elif chance == 'vermelha':
                    print("Oh Não! Uma armadilha de chamas...")
                    print("GAME OVER!")
        
        # Porta amarela
        elif ilha == 'amarela':
            print('Você encontrou o tesouro!!!')
            print('GAME OVER!')
  
    # Nadando
    elif lago == 'nadar':
        print("Penalidade de -5 no dado por estar dentro da água.")
        d20 = random.choice(dado)
        if d20 >= (15):
            print("Um monstro do lago aparece!")
            print(f"Dado = {d20}")
            print("Mesmo dentro d'agua você sempre da um jeito!")
            ilha = input("\nDe alguma forma você chega a ilha. Caminhando um pouco encontra a masmorra, Dentro da masmorra existem três portas, qual você escolhe?\nDigite [Vermelha], [Azul] ou [Amarela]: ").lower()
            clear()
        
            # Porta vermelha
            if ilha == 'vermelha':
                print("Oh Não! Uma armadilha de chamas...")
                print("GAME OVER!")
            
            # Porta azul
            elif ilha == 'azul':
                d20 = random.choice(dado)
                if d20 >= 10:
                    print(f"Dado = {d20}")
                    print("Monstros te atacam! Em um ambiente fechado é uma luta difícil de alguma forma você da um jeito.")
                    chance = input("Escolha outra porta:\nDigite [Vermelha] ou [Amarela]: ").lower()
                    clear()
                    if chance == 'amarela':
                        print('Você encontrou o tesouro!!!')
                        print('GAME OVER!')
                    elif chance == 'vermelha':
                        print("Oh Não! Uma armadilha de chamas...")
                        print("GAME OVER!")
            
            # Porta amarela
            elif ilha == 'amarela':
                print('Você encontrou o tesouro!!!')
                print('GAME OVER!')
                
        else:
            print("Um monstro do lago aparece!")
            print("Você é engolido sem poder fazer nada...")
            print('GAME OVER!')

# Pela direita
elif estrada == 'direita':
    d20 = random.choice(dado)
    if d20 >= 10:
        print(f"Dado = {d20}")
        print("Bandidos te atacam, é uma luta desfavorável mas você da um jeito.\n")
        lago = input(f'Você segue seu caminho a {estrada}. Logo encontra um lago e avista a tão falada ilha. Para chegar na ilha você prefere ir de barco ou ir nadando?\nDigite: [Nadar] ou [Barco]: ')
        clear()

        # Pelo Barco
        if lago == "barco":
            ilha = input("\nCom segurança você chega a ilha. Caminhando um pouco encontra a masmorra, Dentro da masmorra existem três portas, qual você escolhe?\nDigite [Vermelha], [Azul] ou [Amarela]: ").lower()
            clear()
            
            # Porta vermelha
            if ilha == 'vermelha':
                print("Oh Não! Uma armadilha de chamas...")
                print("GAME OVER!")
            
            # Porta azul
            elif ilha == 'azul':
                d20 = random.choice(dado)
                if d20 >= 10:
                    print(f"Dado = {d20}")
                    print("Monstros te atacam! Em um ambiente fechado é uma luta difícil de alguma forma você da um jeito.")
                    chance = input("Escolha outra porta:\nDigite [Vermelha] ou [Amarela]: ").lower()
                    clear()
                    if chance == 'amarela':
                        print('Você encontrou o tesouro!!!')
                        print('GAME OVER!')
                    elif chance == 'vermelha':
                        print("Oh Não! Uma armadilha de chamas...")
                        print("GAME OVER!")
            
            # Porta amarela
            elif ilha == 'amarela':
                print('Você encontrou o tesouro!!!')
                print('GAME OVER!')

        # Nadando    
        elif lago == 'nadar':
            print("Penalidade de -5 no dado por estar dentro da água.")
            d20 = random.choice(dado)
            if d20 >= (15):
                print("Um monstro do lago aparece!")
                print(f"Dado = {d20}")
                print("Mesmo dentro d'agua você sempre da um jeito!")
                ilha = input("\nDe alguma forma você chega a ilha. Caminhando um pouco encontra a masmorra, Dentro da masmorra existem três portas, qual você escolhe?\nDigite [Vermelha], [Azul] ou [Amarela]: ").lower()
                clear()
                # Porta vermelha
                if ilha == 'vermelha':
                    print("Oh Não! Uma armadilha de chamas...")
                    print("GAME OVER!")
                
                # Porta azul
                elif ilha == 'azul':
                    d20 = random.choice(dado)
                    if d20 >= 10:
                        print(f"Dado = {d20}")
                        print("Monstros te atacam! Em um ambiente fechado é uma luta difícil de alguma forma você da um jeito.")
                        chance = input("Escolha outra porta:\nDigite [Vermelha] ou [Amarela]: ").lower()
                        clear()
                        if chance == 'amarela':
                            print('Você encontrou o tesouro!!!')
                            print('GAME OVER!')
                        elif chance == 'vermelha':
                            print("Oh Não! Uma armadilha de chamas...")
                            print("GAME OVER!")
                
                # Porta amarela
                elif ilha == 'amarela':
                    print('Você encontrou o tesouro!!!')
                    print('GAME OVER!')
                    
            else:
                print(f"Dado = {d20}")
                print("Um monstro do lago aparece!")
                print("Você é engolido sem poder fazer nada...")
                print('GAME OVER!')
    
    elif d20 < 10:
        print(f"Dado = {d20}")
        print("Bandidos te atacam, você busca lutar mas são muitos e você não da conta...\nGAME OVER!")