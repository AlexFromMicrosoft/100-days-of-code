import random
import string

# Listas de caracteres
letras = string.ascii_letters
numeros = string.digits
simbolos = string.punctuation

# Inputs
qtd_letras = int(input("Quantidade de letras: "))
qtd_numeros = int(input("Quantidade de números: "))
qtd_simbolos = int(input("Quantidade de símbolos: "))

# Lista das quantidades e listas correspondentes
quantidades = [qtd_letras, qtd_numeros, qtd_simbolos]
listas = [letras, numeros, simbolos]

# Inicialização da senha
senha = []

# Loop para gerar a senha
for i in range(len(quantidades)):
    quantidade = quantidades[i]
    lista = listas[i]
    amostra = random.sample(lista, quantidade)
    senha.extend(amostra)

# Embaralhando a senha final
random.shuffle(senha)

# Convertendo a lista de caracteres em uma string
senha_final = ''.join(senha)

print("Senha gerada:", senha_final)
