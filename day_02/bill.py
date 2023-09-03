# Saudar
# Criar um programa que:
    # Pergunta o valor da conta
    # Pergunta quanto deixará de gorjeta: [10%, 12%, 15%]
    # Pergunta em quantas pessoas irá dividir a conta
    # Realiza o cálculo e mostra quanto deu para cada 1

print("Calculadora da Conta\n")

bill = int(input("Quanto deu a conta?\nR$"))
gorjeta = int(input("Quanto deixará de gorjeta? Digite [10%/12%/15%]: \n").replace("%", ""))
divisao = int(input("Em quantas pessoas irá dividir a conta?\nDigite aqui: "))

porcentagem = (gorjeta / 100) * bill
calc = (bill - porcentagem) / divisao
arredondando = round(calc, 2)

print(f"Dividindo a conta em {divisao} pessoas, tirando a taxa de {gorjeta}% do garçom, cada um deve pagar R${calc}.")

