# ==========================================
# SISTEMA HOSPITALAR
# ==========================================

pacientes = []
consultas = []
farmacia = []


# ==========================================
# CADASTRO DE PACIENTE
# ==========================================

def cadastrar_paciente():
    print("\n===== CADASTRO DE PACIENTE =====")

    nome = input("Nome: ")
    idade = int(input("Idade: "))
    cpf = input("CPF: ")
    telefone = input("Telefone: ")

    paciente = {
        "nome": nome,
        "idade": idade,
        "cpf": cpf,
        "telefone": telefone
    }

    pacientes.append(paciente)

    print("\nPaciente cadastrado com sucesso!")


# ==========================================
# LISTAR PACIENTES
# ==========================================

def listar_pacientes():
    print("\n===== PACIENTES CADASTRADOS =====")

    if len(pacientes) == 0:
        print("Nenhum paciente cadastrado.")
        return

    for i, paciente in enumerate(pacientes, 1):
        print(f"\nPaciente {i}")
        print(f"Nome: {paciente['nome']}")
        print(f"Idade: {paciente['idade']}")
        print(f"CPF: {paciente['cpf']}")
        print(f"Telefone: {paciente['telefone']}")


# ==========================================
# BUSCAR PACIENTE
# ==========================================

def buscar_paciente():
    print("\n===== BUSCAR PACIENTE =====")

    cpf = input("Digite o CPF do paciente: ")

    for paciente in pacientes:
        if paciente["cpf"] == cpf:
            print("\nPaciente encontrado!")
            print(f"Nome: {paciente['nome']}")
            print(f"Idade: {paciente['idade']}")
            print(f"CPF: {paciente['cpf']}")
            print(f"Telefone: {paciente['telefone']}")
            return

    print("\nPaciente não encontrado.")


# ==========================================
# MARCAR CONSULTA
# ==========================================

def marcar_consulta():
    print("\n===== MARCAR CONSULTA =====")

    cpf = input("CPF do paciente: ")

    paciente_encontrado = None

    for paciente in pacientes:
        if paciente["cpf"] == cpf:
            paciente_encontrado = paciente
            break

    if paciente_encontrado is None:
        print("\nPaciente não encontrado.")
        return

    medico = input("Nome do médico: ")
    especialidade = input("Especialidade: ")
    data = input("Data da consulta: ")
    horario = input("Horário: ")

    consulta = {
        "paciente": paciente_encontrado["nome"],
        "cpf": cpf,
        "medico": medico,
        "especialidade": especialidade,
        "data": data,
        "horario": horario
    }

    consultas.append(consulta)

    print("\nConsulta marcada com sucesso!")


# ==========================================
# LISTAR CONSULTAS
# ==========================================

def listar_consultas():
    print("\n===== CONSULTAS =====")

    if len(consultas) == 0:
        print("Nenhuma consulta cadastrada.")
        return

    for i, consulta in enumerate(consultas, 1):
        print(f"\nConsulta {i}")
        print(f"Paciente: {consulta['paciente']}")
        print(f"CPF: {consulta['cpf']}")
        print(f"Médico: {consulta['medico']}")
        print(f"Especialidade: {consulta['especialidade']}")
        print(f"Data: {consulta['data']}")
        print(f"Horário: {consulta['horario']}")


# ==========================================
# CADASTRAR MEDICAMENTO
# ==========================================

def cadastrar_medicamento():
    print("\n===== CADASTRO DE MEDICAMENTO =====")

    nome = input("Nome do medicamento: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: R$ "))

    medicamento = {
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }

    farmacia.append(medicamento)

    print("\nMedicamento cadastrado com sucesso!")


# ==========================================
# LISTAR FARMÁCIA
# ==========================================

def listar_farmacia():
    print("\n===== FARMÁCIA =====")

    if len(farmacia) == 0:
        print("Nenhum medicamento cadastrado.")
        return

    for i, medicamento in enumerate(farmacia, 1):
        print(f"\nMedicamento {i}")
        print(f"Nome: {medicamento['nome']}")
        print(f"Quantidade: {medicamento['quantidade']}")
        print(f"Preço: R$ {medicamento['preco']:.2f}")


# ==========================================
# MENU DA FARMÁCIA
# ==========================================

def menu_farmacia():

    while True:

        print("\n===== FARMÁCIA =====")
        print("1 - Cadastrar medicamento")
        print("2 - Listar medicamentos")
        print("3 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_medicamento()

        elif opcao == "2":
            listar_farmacia()

        elif opcao == "3":
            break

        else:
            print("Opção inválida!")


# ==========================================
# MENU PRINCIPAL
# ==========================================

while True:

    print("\n================================")
    print("       SISTEMA HOSPITALAR")
    print("================================")
    print("1 - Cadastrar paciente")
    print("2 - Listar pacientes")
    print("3 - Buscar paciente")
    print("4 - Marcar consulta")
    print("5 - Listar consultas")
    print("6 - Farmácia")
    print("7 - Sair")
    print("================================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_paciente()

    elif opcao == "2":
        listar_pacientes()

    elif opcao == "3":
        buscar_paciente()

    elif opcao == "4":
        marcar_consulta()

    elif opcao == "5":
        listar_consultas()

    elif opcao == "6":
        menu_farmacia()

    elif opcao == "7":
        print("\nSistema encerrado.")
        break

    else:
        print("\nOpção inválida!")