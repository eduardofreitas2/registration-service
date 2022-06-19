import os
import json

# Função anônima que limpa o console.
clear = lambda: os.system("cls")

# Abre o arquivo txt que será manipulado como banco de dados.
# db = open("db.json", "w")
# db_read = open("db.json", "r")

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
    print("Cadastro de reserva")
    
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
    if nome != "" or cpf != "" or qtde_pessoas != 0 or qtde_dias != 0 or valor != 0:
        print("Favor inserir campos válidos.")
    else:
        reservas.append(reserva)
        print("Cadastro realizado com sucesso!")

    # Converte em JSON e escreve no db.json
    # json_str = json.dumps(reservas)

    # db.write(json_str)

# Função que faz o check-in de usuários com reservas cadastradas.
def check_in():
    print("Check-in")

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

    # try:
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        cadastrar_reserva()
    elif opcao == 2:
        #TESTE
        print(reservas)
        check_in()
    elif opcao == 3:
        print("nhcc")
        # realizar_checkout()
    elif opcao == 4:
        print("nhaccc")
        # atualizar_cadastro()
    elif opcao == 5:
        print("nhoncc")
        # obter_relatorio()
    elif opcao == 6:
        print("nhoncers")
        # finalizar_conexao()
        break
    else:
        raise

    print("Pressione enter para voltar ao menu.")
    input("")
    
    # Exception que retorna o usuário ao menu caso a opção informada não seja válida.
    # except:
        # clear()
        # print("Por favor, digite uma opção válida. (Pressione enter para voltar ao menu)")
        # input("")

    # clear()