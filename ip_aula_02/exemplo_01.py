# Um programa que verifica email e senha
# e informa se o usuário está correto ou não.

email = input("Digite seu email: ")
senha = input("Digite sua senha: ")

if email == "rivotril@example.com" and senha == "123456":
    print("Usuário logado com sucesso!")
else:
    print("Email ou senha incorretos. Tente novamente.")