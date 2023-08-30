# Lista dos inputs
nome_a = []
idade_a = []
sexo_a = []

# Lista das condições
n_homem_velho = []
i_homem_velho = []
mulheres_novas = []

# Laço
for i in range(0, 4):
    print(f"-- {i + 1}ª Pessoa --")
    nome = input("Nome: ").title()
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").upper()

    # Armazenar os valores dos inputs
    nome_a.append(nome)
    idade_a.append(idade)
    sexo_a.append(sexo)

    # Condição para o nome e idade do homem mais velho.
    if sexo_a[i] == "M":
        i_homem_velho.append(idade_a[i])
        n_homem_velho.append(nome_a[i])

    # Condição para mulheres menores de 20 anos.
    if sexo_a[i] == "F":
        if idade_a[i] < 20:
            mulheres_novas.append(idade)

# Qual a média de idade?
soma = sum(idade_a) # Somar as idades da lista.
media = soma / len(idade_a) # Dividir a soma pelo tamanho da lista.
print(f"A média de idade é: {media} anos de idade") # Média de idade

# Quem é o homem mais velho?
idade_max = max(i_homem_velho) # Pegar o maior valor da lista de idade dos homens
nome_max = n_homem_velho[i_homem_velho.index(idade_max)] # Pegar o nome do homem que está na mesma posição da maior idade dos homens
print(f"{nome_max} é o homem mais velho com {idade_max}") # Mostrar quem é o homem mais velho e sua idade

# Quantas são as Mulheres com menos de 20 anos?
tot_mul = (len(mulheres_novas)) # Total de mulheres com menos de 20 anos na lista.
print(f"No total {tot_mul} das mulheres tem menos de 20 anos.") # Mostrar quantas mulheres tem menos de 20 anos.


    

