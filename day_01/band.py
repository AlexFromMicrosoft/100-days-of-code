# Band Name Generator

# O Band Name Generator cria o nome de uma banda se baseando no nome da sua cidade e seu animal de estimação.

cidade = input("Aonde você mora?\n").title()
pet = input("Qual o nome do seu bixinho de estimação?\n").title()

print("Um bom nome para sua banda seria: " + cidade + " " + pet) # Caso 1 - Menos recomendado
print(f"Um bom nome para sua banda seria: {cidade} {pet}") # Caso 2 - Melhor formato
