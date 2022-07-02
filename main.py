import os
import sqlite3

# Conexão com o banco
db = sqlite3.connect('registration-service.db')

# Cursor é utilizado para executar queries.
cursor = db.cursor()

# Função anônima que limpa o console.
clear = lambda: os.system("cls")

# Função que monta a query para buscar a tabela de reservas e converte em lista.
def get_all_reservas():
    cursor.execute("SELECT * FROM reservas")
    reservas = cursor.fetchall()
    reservas_list = list(reservas)

    return reservas_list

# Função que monta a query para buscar somente os valores dos status "finalizados"
def get_reservas_finalizadas():
    cursor.execute("SELECT * FROM reservas WHERE status = 'F'")
    reservas = cursor.fetchall()
    reservas_finalizadas = list(reservas)
    
    return reservas_finalizadas

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
    qtde_pessoas = input("Quantidade de pessoas: ")
    qtde_dias = input("Quantidade de dias: ")
    tipo_quarto = input("Tipo do quarto (S - Standard / D - Deluxe / P - Premium): ").upper()

    # Validações dos campos
    if not (tipo_quarto == "S" or tipo_quarto == "D" or tipo_quarto == "P"):
        return print("Favor inserir um tipo de quarto válido.")

    if nome == "" or cpf == "" or qtde_pessoas == "" or qtde_dias == "" or tipo_quarto == "":
        return print("Favor preencher todos os campos.")


    # Invoca a função calcula_valor que recebe os parâmetros relevantes para calcular o valor.
    valor = calcula_valor(tipo_quarto, int(qtde_pessoas), int(qtde_dias))
    
    cursor.execute(f"INSERT INTO reservas VALUES ('{nome}', '{cpf}', {int(qtde_pessoas)}, {int(qtde_dias)}, '{tipo_quarto}', {valor}, 'R')")
    db.commit()

    print("Cadastro realizado com sucesso!")
    

# Função que faz o check-in de usuários com reservas cadastradas.
def check_in():
    print("Informe um cliente para realizar o Check-in.")

    cpf = input("CPF: ")
    # Itera o array de reservas passando por cada elemento.
    for reserva in reservas_list:
        # Se encontrar um cpf inserido pelo usuário igual a um cpf cadastrado em uma reserva ele confirma se o usuário deseja confirmar o Check-in.
        if cpf == reserva[1]:
            # Se a reserva já for "A - Ativo" ele informa o usuário e retorna ele ao menu.
            if reserva[6] == "A":                
                return print(f"Check-in já realizado para a reserva do cliente {reserva[0]}.")
            elif reserva[6] == "F":
                return print(f"Reserva já finalizada.")

            print("Reserva encontrada!")

            confirmar = input("Confirmar Check-in? (S/N): ").upper()
            # Se o usuário confirmar o Check-in o status da reserva é alterado de "R - Reservado" (Default) para "A - Ativo".
            if confirmar == "S":
                cursor.execute(f"UPDATE reservas SET status = 'A' WHERE cpf = '{cpf}'")
                db.commit()
                print("Check-in realizado com sucesso.")
            else:
                print("Operação cancelada.")

# Função que faz o Check-out de usuários com reservas ativas (Check-in feito).
def check_out():
    print("Informe um cliente para realizar o Check-out.")

    cpf = input("CPF: ")
    # Itera o array de reservas passando por cada elemento.
    for reserva in reservas_list:
        # Se encontrar um cpf inserido pelo usuário igual a um cpf cadastrado em uma reserva ele confirma se o usuário deseja confirmar o Check-out.
        if cpf == reserva[1]:
            # Se a reserva já for "F - Finalizado", "R - Reservado" ou "C - Cancelado" ele informa o usuário e retorna ele ao menu.
            if not reserva[6] == "A":
                return print(f"Não há Check-ins para o cliente {reserva[0]}.")

            print("Check-in encontrado!")

            confirmar = input("Confirmar Check-out? (S/N): ").upper()
            # Se o usuário confirmar o Check-in o status da reserva é alterado de "R - Reservado" (Default) para "A - Ativo".
            if confirmar == "S":
                cursor.execute(f"UPDATE reservas SET status = 'F' WHERE cpf = '{cpf}'")
                db.commit()
                print("Check-out realizado com sucesso.")
            else:
                print("Operação cancelada.")

# Função que atualiza os dados de uma reserva.
def atualizar_reserva():
    print("Informe um cliente para atualizar os dados da reserva.")

    cpf = input("CPF: ")
    # Itera o array de reservas passando por cada elemento.
    for reserva in reservas_list:
        # Se encontrar um cpf inserido pelo usuário igual a um cpf cadastrado o usuário consegue alterar e confirmar alterações de dados da reserva.
        if cpf == reserva[1]:
            print("Informe os dados que deseja alterar da reserva.")

            qtde_pessoas = input("Quantidade de pessoas: ")
            qtde_dias = input("Quantidade de dias: ")
            tipo_quarto = input("Tipo do quarto (S - Standard / D - Deluxe / P - Premium): ")
            status = input("Status (R - Reservado / C - Cancelado / A - Ativo, F - Finalizado): ")

            # Validações dos campos
            if not (status == "R" or status == "C" or status == "A" or status == "F"):
                return print("Favor inserir um status válido.")
            elif not (tipo_quarto == "S" or tipo_quarto == "D" or tipo_quarto == "P"):
                return print("Favor inserir um tipo de quarto válido.")

            if qtde_pessoas == "" or qtde_dias == "" or tipo_quarto == "" or status == "":
                return print("Favor preencher todos os campos.")

            # Invoca a função calcula_valor que recebe os parâmetros relevantes para calcular o valor.
            valor = calcula_valor(tipo_quarto, int(qtde_pessoas), int(qtde_dias))

            confirmar = input("Confirmar alterações? (S/N): ")
            # Se o usuário confirmar as alterações os dados anteriores são sobrescritos pelos novos.
            if confirmar == "S":
                # Atribui os novos valores da reserva a cada propriedade.
                cursor.execute(f"UPDATE reservas SET qtde_pessoas = {qtde_pessoas}, qtde_dias = {qtde_dias}, tipo_quarto = '{tipo_quarto}', valor = {valor}, status = '{status}' WHERE cpf = '{cpf}'")
                db.commit()

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

        cursor.execute("SELECT * FROM reservas WHERE status = 'R'")
        rows = cursor.fetchall()

        for row in rows: 
            print(row)
    elif opcao == 2:
        print("Reservas com Status 'C - Cancelado'.")

        cursor.execute("SELECT * FROM reservas WHERE status = 'C'")
        rows = cursor.fetchall()

        for row in rows: 
            print(row)
    elif opcao == 3:
        print("Reservas com Status 'A - Ativo'.")
        
        cursor.execute("SELECT * FROM reservas WHERE status = 'A'")
        rows = cursor.fetchall()

        for row in rows: 
            print(row)
    elif opcao == 4:
        print("Reservas com Status 'F - Finalizado'.")
        
        cursor.execute("SELECT * FROM reservas WHERE status = 'F'")
        rows = cursor.fetchall()

        for row in rows: 
            print(row)
    elif opcao == 5:
        reservas_finalizadas = get_reservas_finalizadas()

        print("Total recebido de todas as reservas.")

        total = 0
        
        for reserva in reservas_finalizadas:
            total = total + reserva[5]

        print(f"R$: {total}")
    elif opcao == 6:
        print("Informe o CPF do cliente para consultar suas reservas.")

        cpf = input("CPF: ")

        cursor.execute(f"SELECT * FROM reservas WHERE cpf = '{cpf}'")
        rows = cursor.fetchall()

        for row in rows:
            print(row)
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
    reservas_list = get_all_reservas()
    # print(reservas_list) # Informação de testes para conseguir visualizar as reservas cadastradas.

    if opcao == 1:
        cadastrar_reserva()
    elif opcao == 2:
        check_in()
    elif opcao == 3:
        check_out()
    elif opcao == 4:
        atualizar_reserva()
    elif opcao == 5:
        imprimir_relatorio()
    elif opcao == 6:
        break
    else:
        clear()
        print("Favor inserir um valor existente.")

    print("Pressione enter para voltar ao menu.")
    input("")

    clear()