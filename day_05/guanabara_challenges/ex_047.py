# Números pares entre 1 e 50.

print("Os valores pares entre 1 e 50 são: {", end="")
# Laço i no range entre 1 e 50.
for i in range(1, 50 + 1):
    # Se o módulo entre i e 2 == 0, i é par já que é múltiplo de 2.
    # Se i é par imprima seu valor na tela.
    if i % 2 == 0 and i < 50:
        print(i, end=", ")
    if i == 50:
        print(i, end="")
print("}")