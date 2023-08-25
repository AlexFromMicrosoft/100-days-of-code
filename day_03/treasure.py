print("Bem vindo a Treasure Island!")
print("Sua missão é encontrar o tesouro da ilha.") 

#Write your code below this line 👇

# Na estrada direita ou esquerda direita mata
espada = True
road = input("Em sua viagem, você encontra uma bifurcação na estrada. Qual lado seguir? \nDigite 'Direita' ou 'Esquerda'").lower()
if road == "esquerda":
    lago = input("O caminho te leva a um lago que o separa da ilha. Você espera por um barco ou vai nadando? \nDigite 'Nadar' ou 'Esperar'").lower()
    if lago == "esperar":
        ilha = input("Você aguarda um pouco e logo um baqueiro aparece. Você chega em segurança a ilha e avista a masmorra. \nNa masmorra há três portas você decide por ir pela... \nDigite 'Vermelha' , 'Azul' ou 'Amarela'")
        if ilha == "vermelha":
            print("Oh Não! Uma armadilha de fogo... \nGAME OVER")
        elif ilha == "azul":
            print("Monstros apareceram você luta e vence mas sua espada se quebrou, Você tenta outra porta.")
            porta = input("Digite 'vermelha' ou 'amarela'")
            if porta == "vermelha":
                print("Oh Não! Uma armadilha de fogo... \nGAME OVER")
            else: 
                print("Você encontrou o Tesouro! Parabéns!")
        elif ilha == "amarela":
            print("Você encontrou o Tesouro! Parabéns!")
    else:
        print("OH Não um monstro, seus movimentos são limitados na água você consegue sair vivo mas sua espada se quebrou :C")
        espada = False
        ilha = input("Você nada mais um pouco e logo você chega à ilha e avista a masmorra. \nNa masmorra há três portas você decide por ir pela... \nDigite 'Vermelha' , 'Azul' ou 'Amarela'")
        if ilha == "vermelha":
            print("Oh Não! Uma armadilha de fogo... \nGAME OVER")
        elif ilha == "azul":
            print("Monstros apareceram você tenta lutar mas sem sua espada não há como vencer \nGAME OVER")
        elif ilha == "amarela":
            print("Você encontrou o Tesouro! Parabéns!")
else:
    print("Haviam bandidos na estrada, você lutou bravamente mas sua espada se quebrou :C")
    espada = False
    lago = input("O caminho te leva a um lago que o separa da ilha. Você espera por um barco ou vai nadando? \nDigite 'Nadar' ou 'Esperar'").lower()
    if lago == "esperar":
        ilha = input("Você aguarda um pouco e logo um baqueiro aparece. Você chega em segurança a ilha e avista a masmorra. \nNa masmorra há três portas você decide por ir pela... \nDigite 'Vermelha' , 'Azul' ou 'Amarela'")
        if ilha == "vermelha":
            print("Oh Não! Uma armadilha de fogo... \nGAME OVER")
        elif ilha == "azul":
            print("Monstros apareceram você tenta lutar mas sem sua espada não há como vencer \nGAME OVER")
        elif ilha == "amarela":
            print("Você encontrou o Tesouro! Parabéns!")
    else:
        print("OH Não um monstro! Sem sua espada não há como lutar...\nGAME OVER")

# No lago nadar ou esperar um barco? nadar é atacado por monstro do lago

# Na casa da ilha tem 3 portas vermelha, amarela ou azul? verm =fogo azul = monst amarelo é win
