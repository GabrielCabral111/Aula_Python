# Lista que vai armazenar os dados
usuarios = []

# CREATE
def criar_usuario(nome):
    usuarios.append(nome)
    print(f"Usuário '{nome}' criado com sucesso!")

# READ
def listar_usuarios():
    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado.")
    else:
        print("Lista de usuários:")
        for i, usuario in enumerate(usuarios):
            print(f"{i} - {usuario}")

# UPDATE
def atualizar_usuario(indice, novo_nome):
    if 0 <= indice < len(usuarios):
        usuarios[indice] = novo_nome
        print("Usuário atualizado com sucesso!")
    else:
        print("Índice inválido.")

# DELETE
def deletar_usuario(indice):
    if 0 <= indice < len(usuarios):
        removido = usuarios.pop(indice)
        print(f"Usuário '{removido}' removido!")
    else:
        print("Índice inválido.")

# MENU
while True:
    print("\n1 - Criar usuário")
    print("2 - Listar usuários")
    print("3 - Atualizar usuário")
    print("4 - Deletar usuário")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome: ")
        criar_usuario(nome)

    elif opcao == "2":
        listar_usuarios()

    elif opcao == "3":
        listar_usuarios()
        indice = int(input("Digite o índice do usuário: "))
        novo_nome = input("Novo nome: ")
        atualizar_usuario(indice, novo_nome)

    elif opcao == "4":
        listar_usuarios()
        indice = int(input("Digite o índice do usuário: "))
        deletar_usuario(indice)

    elif opcao == "5":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")