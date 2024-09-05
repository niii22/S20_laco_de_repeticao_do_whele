"""
CALCULANDO A MÉDIA DAS NOTAS
"""

soma = 0
contagem = 0

while True:
    nota = float(input("Digite uma nota (ou -1 para terminar): ")) # arredondando resultado para  2 casas decimais após a vírgula
    if nota == -1: # se digitar -1
        break # então o programa encerra e calcula a nota
    soma += nota # somar 0 + digitado pelo usuário
    contagem += 1 # conta a quantidade de notas para calcular a média.

if contagem > 0: # se tiver alguma notas
    media = soma / contagem #  a varíavel media recebe o cálculo da soma das notas pela quantidade de notas
    print(f"A média das notas é: {media:.2f}") # arredondando resultado para até 2 casas decimais ápos a vírgula
else:
    print("Nenhuma nota foi inserida.")