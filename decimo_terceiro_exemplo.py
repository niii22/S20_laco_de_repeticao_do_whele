"""
CONTAR VOGAIS
"""
while True:
    palavra = input("Digite uma palavra (ou pressione Enter para sair): ")
    if palavra == "": # Se não tiver palavras, por isso enter direto.
        break # se não contar nenhuma palavra então para.

    vogais = "aeiouAEIOU" # Estou ensinando o algoritmo a reconhecer vogais
    contagem_vogais = sum(1 for letra in palavra if letra in vogais)
    """
    A variável contagem_vogais contém uma função de soma (sum) que atribui o número 1
para cada vogal prente na variável vogais para depois somar."""
    print(f"A palavra '{palavra}' tem {contagem_vogais} vogais.")