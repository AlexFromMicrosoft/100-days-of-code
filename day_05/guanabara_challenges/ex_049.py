# Tabuada.
user = int(input("Qual tabuada deseja?"))
for i in range(1, 10 + 1):
    tab = user * i
    print(f"{user} x {i} = {tab}")