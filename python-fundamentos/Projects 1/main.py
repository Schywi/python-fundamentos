from usuario import Usuario

continuar = 1
lista_usuarios = []

while continuar != 0:
     try:
        nome = input("Digite o seu nome: ")
        idade = int(input("Digite sua idade: "))
        sobrenome = input("Digite seu sobrenome: ")
        usuario = Usuario(nome, idade, sobrenome)
        lista_usuarios.append(usuario)

        if idade == 99:
            break
        if idade ==98:
            continue

        print(f"Olá, {usuario.nome} {usuario.sobrenome}, sua idade é {usuario.idade}")

        if idade < 17:
            print(f"{usuario.nome} é adolecente")
        elif idade >= 17 and idade <= 58:
            print(f"{usuario.nome} é adulto ")
        else:
            print(f"{usuario.nome} é idoso ")
        continuar = int(input("Deseja continuar cadastrando?  Digite 0 para Sair ou 1 para continuar: "))

     except ValueError:
        print("Você deve informar um número válido")
else:
    print("Lista de usuários cadstrados: ")

    for x in lista_usuarios:
        print(f"Nome completo: {x.nome} {x.sobrenome} - idade {x.idade}")

    print("O loop entrou no else")

