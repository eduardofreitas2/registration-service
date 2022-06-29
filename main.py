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

# Função que calcula o valor da reserva conforme o tipo do quarto, número de pessoas e quantidade de dias.
def calcula_valor(tipo_quarto, qtde_pessoas, qtde_dias):
    if tipo_quarto == "S":
        valor = ((100 * qtde_pessoas) * qtde_dias)
    elif tipo_quarto == "D":
        valor = ((200 * qtde_pessoas) * qtde_dias)
    elif tipo_quarto == "P":
        valor = ((300 * qtde_pessoas) * qtde_dias)

    return valor

# Função que realiza o cadastro de uma reserva.
def cadastrar_reserva():
    print("Informe os dados do cliente para cadastrar a reserva.")
    
    nome = input("Nome: ")
    cpf = input("CPF: ")
    qtde_pessoas = int(input("Quantidade de pessoas: "))
    qtde_dias = int(input("Quantidade de dias: "))
    tipo_quarto = input("Tipo do quarto (S - Standard / D - Deluxe / P - Premium): ")

    # Invoca a função calcula_valor que recebe os parâmetros relevantes para calcular o valor.
    valor = calcula_valor(tipo_quarto, qtde_pessoas, qtde_dias)

    # Aqui, são atribuidos os valores informados pelo usuário a cada propriedade da reserva.
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
    print("Informe um cliente para realizar o Check-in.")

    cpf = input("CPF: ")
    # Itera o array de reservas passando por cada elemento.
    for reserva in reservas:
        # Se encontrar um cpf inserido pelo usuário igual a um cpf cadastrado em uma reserva ele confirma se o usuário deseja confirmar o Check-in.
        if cpf == reserva['cpf']:
            # Se a reserva já for "A - Ativo" ele informa o usuário e retorna ele ao menu.
            if reserva['status'] == "A":
                print(f"Check-in já realizado para a reserva do cliente {reserva['nome']}.")
                
                continue

            print("Reserva encontrada!")

            confirmar = input("Confirmar Check-in? (S/N): ")
            # Se o usuário confirmar o Check-in o status da reserva é alterado de "R - Reservado" (Default) para "A - Ativo".
            if confirmar == "S":
                reserva['status'] = "A"

                print("Check-in realizado com sucesso.")
            else:
                print("Operação cancelada.")

# Função que faz o Check-out de usuários com reservas ativas (Check-in feito).
def check_out():
    print("Informe um cliente para realizar o Check-out.")

    cpf = input("CPF: ")
    # Itera o array de reservas passando por cada elemento.
    for reserva in reservas:
        # Se encontrar um cpf inserido pelo usuário igual a um cpf cadastrado em uma reserva ele confirma se o usuário deseja confirmar o Check-out.
        if cpf == reserva['cpf']:
            # Se a reserva já for "F - Finalizado", "R - Reservado" ou "C - Cancelado" ele informa o usuário e retorna ele ao menu.
            if reserva['status'] == "F" or reserva['status'] == "R" or reserva['status'] == "C":
                print(f"Não há Check-ins para o cliente {reserva['nome']}.")
                
                continue

            print("Check-in encontrado!")

            confirmar = input("Confirmar Check-out? (S/N): ")
            # Se o usuário confirmar o Check-in o status da reserva é alterado de "R - Reservado" (Default) para "A - Ativo".
            if confirmar == "S":
                reserva['status'] = "F"

                print("Check-out realizado com sucesso.")
            else:
                print("Operação cancelada.")

def atualizar_reserva():
    print("Informe um cliente para atualizar os dados da reserva.")

    cpf = input("CPF: ")
    # Itera o array de reservas passando por cada elemento.
    for reserva in reservas:
        # Se encontrar um cpf inserido pelo usuário igual a um cpf cadastrado o usuário consegue alterar e confirmar alterações de dados da reserva.
        if cpf == reserva['cpf']:
            print("Informe os dados que deseja alterar da reserva.")

            qtde_pessoas = int(input("Quantidade de pessoas: "))
            qtde_dias = int(input("Quantidade de dias: "))
            tipo_quarto = input("Tipo do quarto (S - Standard / D - Deluxe / P - Premium): ")

            # Invoca a função calcula_valor que recebe os parâmetros relevantes para calcular o valor.
            valor = calcula_valor(tipo_quarto, qtde_pessoas, qtde_dias)

            confirmar = input("Confirmar alterações? (S/N): ")
            # Se o usuário confirmar as alterações os dados anteriores são sobrescritos pelos novos.
            if confirmar == "S":
                # Atribui os novos valores da reserva a cada propriedade.
                reserva['qtde_pessoas'] = qtde_pessoas
                reserva['qtde_dias'] = qtde_dias
                reserva['tipo_quarto'] = tipo_quarto
                reserva['valor'] = valor

                print("Dados alterados com sucesso.")
            else:
                print("Operação cancelada.")

# Função que imprime no console os dados relevantes aquilo que o usuário procura.
def imprimir_relatorio():
    print("1 - Relatório de todas as reservas com status R")
    print("2 - Relatório de todas as reservas com status C")
    print("3 - Relatório de todas as reservas com status A")
    print("4 - Relatório de todas as reservas com status F")
    print("5 - Relatório total recebido")
    print("6 - Relatório de reserva por pessoa")
    print("7 - Voltar ao menu")

    opcao = int(input("Digite a opção desejada: "))

    clear()

    if opcao == 1:  
        print("Reservas com Status 'R - Reservado'.")
        for reserva in reservas:
            if reserva['status'] == "R":
                print(reserva)
    elif opcao == 2:
        print("Reservas com Status 'C - Cancelado'.")
        for reserva in reservas:
            if reserva['status'] == "C":
                print(reserva)
    elif opcao == 3:
        print("Reservas com Status 'A - Ativo'.")
        for reserva in reservas:
            if reserva['status'] == "A":
                print(reserva)
    elif opcao == 4:
        print("Reservas com Status 'F - Finalizado'.")
        for reserva in reservas:
            if reserva['status'] == "F":
                print(reserva)
    elif opcao == 5:
        print("Total recebido de todas as reservas.")

        total = 0
        
        for reserva in reservas:
            total = total + reserva['valor']

        print(f"R$: {total}")
    elif opcao == 6:
        print("Informe o CPF do cliente para consultar suas reservas.")

        cpf = input("CPF: ")
        
        for reserva in reservas:
            if cpf == reserva['cpf']:
                print(reserva)
    elif opcao == 7:
        return
    else:
        print("Favor inserir um valor existente.")

# Menu de navegação dos processos do sistema.
while True:
    print("1 - Cadastrar uma reserva")
    print("2 - Entrada do cliente (Check in)")
    print("3 - Saída do cliente (Check out)")
    print("4 - Alterar reserva")
    print("5 - Relatórios")
    print("6 - Sair")

    opcao = int(input("Digite a opção desejada: "))

    clear()
    print(reservas) # Informação de testes para conseguir visualizar as reservas cadastradas.

    if opcao == 1:
        cadastrar_reserva()
    elif opcao == 2:
        check_in()
    elif opcao == 3:
        check_out()
    elif opcao == 4:
        atualizar_reserva()
    elif opcao == 5:
        print("e")
        imprimir_relatorio()
    elif opcao == 6:
        break
    else:
        clear()
        print("Favor inserir um valor existente.")

    print("Pressione enter para voltar ao menu.")
    input("")

    clear()