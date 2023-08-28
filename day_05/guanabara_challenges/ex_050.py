# Soma dos inputs pares.
soma = 0
for i in range(1, 6 + 1):
    user = int(input(f"Digite o valor[{i}]"))
    if user % 2 == 0:
        soma += user
print(soma)