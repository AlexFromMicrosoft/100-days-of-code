print("Bem vindo a Treasure Island!")
print("Sua missão é encontrar o tesouro da ilha.") 

#Write your code below this line 👇

# Inicio da Jornada
road = input("Em sua viagem, você encontra uma bifurcação na estrada. Qual lado seguir? \nDigite 'Direita' ou 'Esquerda'").lower()

# Escolhendo a Esquerda:
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
        ilha = input("Você nada mais um pouco e logo você chega à ilha e avista a masmorra. \nNa masmorra há três portas você decide por ir pela... \nDigite 'Vermelha' , 'Azul' ou 'Amarela'")
        if ilha == "vermelha":
            print("Oh Não! Uma armadilha de fogo... \nGAME OVER")
        elif ilha == "azul":
            print("Monstros apareceram você tenta lutar mas sem sua espada não há como vencer \nGAME OVER")
        elif ilha == "amarela":
            print("Você encontrou o Tesouro! Parabéns!")

#Escolhendo a Direita:
else:
    print("Haviam bandidos na estrada, você lutou bravamente mas sua espada se quebrou :C")
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

