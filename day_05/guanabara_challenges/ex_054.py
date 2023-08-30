users = []
# Loop de inputs:
for i in range(1, 7+1):
    entry = int(input(f"Digite o ano de nascimento do {i}º participante: "))
    users.append(entry)

# Lista para armazenar quem é maior e quem é menor:
maior = []
menor = []

# Loop para armazenar nas listas valores < 21 para maior de idade e > 21 para menor de idade:
for n in range(0, len(users)):
    if (2022 - users[n] > 21):
        maior.append(users[n])
    else:
        menor.append(users[n])

# Mostar na tela o resultado:
print(f"Ao todo tivemos {len(maior)} pessoas maiores de idade")
print(f"E também tivemos {len(menor)} pessoas menores de idade")


