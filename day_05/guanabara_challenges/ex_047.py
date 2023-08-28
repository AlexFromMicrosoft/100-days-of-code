
print("Os valores pares entre 1 e 50 são: {", end="")
for i in range(1, 50 + 1):

    if i % 2 == 0 and i < 50:
        print(i, end=", ")
    if i == 50:
        print(i, end="")
print("}")