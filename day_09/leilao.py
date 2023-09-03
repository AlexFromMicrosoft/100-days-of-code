from art import logo
from clear import clear

print(logo)

lances = {}
end = False

while not end:
    nome = input("Digite seu nome: ").title()
    lance = input("Digite seu lance: $")
    lances[nome] = lance

    novo_participante = input("Existe outro participante? Digite[sim/não]: ")
    if novo_participante == 'nao' or novo_participante == 'não':
        end = True
    elif novo_participante == 'sim':
        clear()

print(lances)novo_participante == 'nao'













