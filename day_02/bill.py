# Saudar
print('')
# Obter valores
bill = input("Quanto deu a conta? ")
percentage = input("Quanto deixará de gorjeta? ")
people =input("Vai dividir em quantas pessoas? ")
# Transformar valores
bill_sif = bill.replace(bill[0], "", 1)
bill_num = float(bill_sif)
percentage_num = float(percentage)
people_num = float(people)
# Calcular
percentage_convert = (bill_num / 100) * percentage_num
res = round((bill_num + percentage_convert) / people_num, 2)
# Imprimir
print(f"Cada pessoa deverá pagar: {res}")