"""
TABUADA
"""

while True:
    numero = int(input("Digite um número para ver a tabuada (0 para sair): "))
    if numero == 0: # se o número digitado for 0
        break # o programa para qaundo digitamos 0
    for i in range(1, 11): 
        """ 
         a variável i significa o intervalo númerico do range que inícia de zero até o último número correspondente ao intervalo do range.
        """
        print(f"{numero} x {i} = {numero * i}")

        """ 
        Será mostrada a tabuada na tela 
        """