users = {}

def cadastrar_usuario():
    user = input("Digite o nome de usuário: ").lower().strip()

    if user in users:
        print("O usuário não pode ser cadastrado")
    else:
        x = input("digite a senha: ").lower().strip()
        y = input("confirme a senha: ").lower().strip()

        if x == y:
            users[user] = x
            print("Usuário cadastrado")
        else:
            print("senhas incompatíveis")



def autenticar_usuario():

    user = input("Digite o nome de usuário: ").lower().strip()


    if user in users:
        senha = input("Digite a senha: ").lower().strip()

        if users[user] == senha: 
            print("Acesso autorizado!")
        else:
            senha = input("tente a senha novamente: ").lower().strip()

            if senha == users[user]:
                print("acesso autorizado!")
            else:
                senha = input("tente a senha novamente: ").lower().strip()
                
                if senha == users[user]:
                    print("acesso autorizado!")
                else:
                    print("acesso negado!")
    else:
        print("este usuário não existe")
        
        
    
condition = True

while condition:
    option = int(input('''

----- Usuários -----
- Para fazer login  [1]
- Cadastrar usuário [2]
- Listar usuários   [3]
- Sair              [4]
\n
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
