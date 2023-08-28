# Identificador de Número Primo
import math

user = int(input("Digite um número: "))
if user <= 1:
    primo = False
if user > 1:
    primo = True
    for i in range(2, math.isqrt(user) + 1):
        if user % i == 0:
            primo = False
            break
if primo:
    print("É primo")
else:
    print("Não é primo")


