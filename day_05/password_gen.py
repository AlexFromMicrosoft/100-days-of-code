# Password Generator
# Imports
import random
import string

print("Seja Bem vindo ao Password Generator!")
# Lista de Caracteres
let = string.ascii_letters
num = string.digits
sym = string.punctuation

# Lista de Input
input_let = int(input("quantas letras terá sua senha?\n".title()))
input_num = int(input("quantos números terá sua senha?\n".title()))
input_sym = int(input("quantos símbolos terá sua senha?\n".title()))

# Lista das Listas
char = [let, num, sym]
entry = [input_let, input_num, input_sym]
lista = []

# Laço
for i in range(len(entry)):
    char_var = char[i]
    entry_var = entry[i]
    amostra = random.sample(char_var, entry_var)
    lista.extend(amostra)

# Shuffle
random.shuffle(lista)

# Formatação da Lista
formatar = (''.join(lista))

# Resultado
print(f"sua nova senha é: {formatar}")