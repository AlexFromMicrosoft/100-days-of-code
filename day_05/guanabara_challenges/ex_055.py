lista = []
for i in range(1, 5 + 1):
    entry = input(f"digite o peso da {i}º pessoa:".title())
    lista.append(entry)

maior = min(lista)
menor = max(lista)

print(f"O maior peso foi de: {maior}Kg")
print(f"O menor peso foi de: {menor}Kg")

