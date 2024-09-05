"""
ESCOLHENDO A OPÇÃO
"""

while True: # enquanto for Verdadeiro
    print("\nMenu:")
    print("1. Pizza 1")
    print("2. Esfira 2")
    print("3. Kibe 3")
    print("4. coxinha 4")
    print("0. sair")
    
    escolha = input("Escolha uma opção: ") # a variável escolha receberá o dado digitado pelo usuário
    
    if escolha == '0': # se a escolha for igual a 0
        print("...::: Saindo :::...") #Mostrar saindo
        break # O programa foi interrompido de acordo com a condição
    elif escolha == '1':
        print("Você escolheu a Pizza 1!")
    elif escolha == '2':
        print("Você escolheu a Esfira 2!")
    elif escolha == '3':
        print("Você escolheu o Kibe 3!")
    elif escolha == '4':
        print( print("Você escolheu a coxinha 4!"))
    else:
        print("Opção inválida! Tente novamente.")