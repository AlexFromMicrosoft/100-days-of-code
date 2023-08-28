# Soma dos ímpares múltiplos de 3 entre 1 e 500.
soma = 0
for i in range(1, 500 + 1):
    if i % 2 != 0 and i % 3 == 0: 
        soma += i 
print(f"A soma dos ímpares múltiplos de 3 entre 1 e 500 é: {soma}.".title())
    
""" 
Explicação:
    - O Laço abrange de 1 a 500. O +1 é para incluir o 500.
    - Foi utilizado o conectivo "and" para que apenas se ambas as proposições forem verdadeiras o if geral é executado.
    - A primeira condição é: Se o módulo do laço/2 for diferente de 0 ele não é par por que todo par é divisível por 2.
    - A segunda condição é: Se o módulo do laço/3 retorna 0, ele é divisível por 3 logo é múltiplo.
    - Quando ambas as proposições são verdadeiras o código ira somar o valor ímpar múltiplo de 3 a variável soma.
    - A saída print irá dar o valor da soma quando o laço chegar no final do seu range.
"""