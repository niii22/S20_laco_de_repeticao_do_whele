"""
LOGIN SIMPLES
"""

usuario_correto ="admin" # o usúario deverá ser este
senha_correta = "1234" # a senha deverá ser esta

while True: # enquanto estiver na lista (enquanto for verdadeiro)
    usuario = input("Nome de usuário: ") # receber o usúario
    senha = input("Senha: ") # receber a senha
    
    if usuario == usuario_correto and senha == senha_correta: # se o usúario e a senha estiverem correta
     print("Login bem-sucedido!")# se estiver correto
    break  #se estiver correto o sistema para.
else : # senão,caso contrario, por outro lado...
 print("Usuário ou senha incorretos! Tente novamente.") # o usúario tentará novamente.