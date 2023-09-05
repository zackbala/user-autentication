users = {}

def cadastrar_usuario():
    user = input("Digite o nome de usuário: ").lower().strip()

    if user in users:
        print("O usuário não pode ser cadastrado")
    else:
        users[user] = input("Digite a senha do novo usuário: ").lower().strip()
        print("Usuário cadastrado")

def autenticar_usuario():
    user = ("Digite o nome de usuário: ").lower().strip()

    if user in users and users[user] ==  input("Digite a senha: ").lower().strip():
        print("Acesso autorizado!")
    else:
        print("Usuário ou senha incorretos")
    
condition = True

while condition:
    option = int(input('''

----- Usuários -----
- Para fazer login  [1]
- Cadastrar usuário [2]
- Listar usuários   [3]
- Sair              [4]

'''))

    if option == 1:
        autenticar_usuario()
    elif option == 2:
        cadastrar_usuario()
    elif option == 3:
        print(users)
    elif option == 4:
        condition = False
    else:
        print("Opção inválida")
