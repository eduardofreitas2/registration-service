import os

# Função anônima que limpa o console.
clear = lambda: os.system("cls")

# Array global das reservas.
reservas = []

# Objeto da reserva passando o tipo e nome dos atributos que deverão ser informados.
reserva = {
    "nome": "",
    "cpf": "",
    "qtde_pessoas": 0,
    "qtde_dias": 0,
    "tipo_quarto": "S",
    "valor": 0,
    "status": "R"
}

# Função que realiza o cadastro de uma reserva.
def cadastrar_reserva():
    print("Informe os dados do cliente para cadastrar a reserva.")
    
    nome = input("Nome: ")
    cpf = input("CPF: ")
    qtde_pessoas = int(input("Quantidade de pessoas: "))
    qtde_dias = int(input("Quantidade de dias: "))
    tipo_quarto = input("Tipo do quarto (S - Standard / D - Deluxe / P - Premium): ")

    # Condição que calcula o valor da reserva conforme o tipo do quarto, número de pessoas e quantidade de dias.
    if tipo_quarto == "S":
        valor = ((100 * qtde_pessoas) * qtde_dias)
    elif tipo_quarto == "D":
        valor = ((200 * qtde_pessoas) * qtde_dias)
    elif tipo_quarto == "P":
        valor = ((300 * qtde_pessoas) * qtde_dias)
    
    reserva = {
        "nome": nome,
        "cpf": cpf,
        "qtde_pessoas": qtde_pessoas,
        "qtde_dias": qtde_dias,
        "tipo_quarto": tipo_quarto,
        "valor": valor,
        "status": "R"
    }

    # Validação dos campos obrigatórios
    if nome == "" or cpf == "":
        print("Favor preencher todos os campos.")
    else:
        reservas.append(reserva)
        print("Cadastro realizado com sucesso!")
    

# Função que faz o check-in de usuários com reservas cadastradas.
def check_in():
    print("Informe um cliente para realizar o Check-in")

    cpf = input("CPF: ")

    for reserva in reservas:
        if cpf == reserva['cpf']:
            print(cpf, reserva['cpf'])

# Menu de navegação dos processos do sistema.
while True:
    print("1 - Cadastrar uma reserva")
    print("2 - Entrada do cliente (Check in)")
    print("3 - Saída do cliente (Check out)")
    print("4 - Alterar reserva")
    print("5 - Relatórios")
    print("6 - Sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        clear()
        cadastrar_reserva()
    elif opcao == 2:
        #TESTE
        clear()
        print(reservas)
        check_in()
    elif opcao == 3:
        clear()
        print("c")
        # check_out()
    elif opcao == 4:
        clear()
        print("d")
        # atualizar_reserva()
    elif opcao == 5:
        clear()
        print("e")
        # imprimir_relatorio()
    elif opcao == 6:
        break
    else:
        clear()
        print("Favor inserir um valor existente.")

    print("Pressione enter para voltar ao menu.")
    input("")

    clear()