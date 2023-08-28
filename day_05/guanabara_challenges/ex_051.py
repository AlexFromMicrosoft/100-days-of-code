# Programa PA
a1 = int(input("Qual o primeiro valor: ")) 
an = int(input("Até onde contar: "))
r = int(input("Qual a razão da PA: "))

print("A PA é: {", end="") 

for pa in range(a1, an + 1, r):
    if pa != a1: # Se a PA não for a1 adcione uma vírgula no final da String.
        print(",", end="")
    print(pa, end="") # Após exibir o valor de pa não quebre a linha graças a end=""
print("}") 
    