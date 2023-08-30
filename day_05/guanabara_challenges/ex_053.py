import unidecode

# Input do Usuário
user = input("Digite uma frase:\n")
# Formatar texto [Remover espaços, acentos, letras maiúsculas]
user_f = unidecode.unidecode(user.lower().replace(" ", ""))
# Transformar a String do input em uma lista de caractéres
lista = list(user_f)

tras = []

# Inverter a lista
for i in range(len(lista) - 1, -1, -1):
    tras.append(lista[i])
print(lista)
print(tras)

# Comparar as listas
if lista == tras:
    print("Isso é um palíndromo")
else:
    print("Isso não é um palíndromo")