import json
from gerente import Gerente
from funcionario import Funcionario
from cliente import Cliente
from carro import Carro

def login():
    # Realiza login e redireciona para o menu correto.
    while True:
        tipo = input("Você é Gerente, Funcionário ou Cliente? (G/F/C) (S para sair): ").strip().upper()
        if tipo == "S":
            print("Saindo do sistema.")
            break

        if tipo == "G":
            cpf = input("Digite seu CPF: ").strip()
            gerente = Gerente.verificar_gerente(cpf)
            if gerente:
                print(f"Gerente {gerente.nome} autenticado com sucesso!\n")
                menu_gerente(gerente)
            else:
                print("Gerente não encontrado.")
                opcao = input("Deseja cadastrar um gerente? (S/N): ").strip().upper()
                if opcao == "S":
                    novo = Gerente.cadastrar_gerente()
                    if novo:
                        # após cadastro chama menu do gerente
                        menu_gerente(novo)

        elif tipo == "F":
            cpf = input("Digite seu CPF: ").strip()
            funcionario = Funcionario.verificar_funcionario(cpf)
            if funcionario:
                print(f"Funcionário {funcionario.nome} autenticado com sucesso!\n")
                menu_funcionario(funcionario)
            else:
                print("Funcionário não encontrado.")
                opcao = input("Deseja se cadastrar como funcionário? (S/N): ").strip().upper()
                if opcao == "S":
                    novo = Funcionario.cadastrar_funcionario()
                    if novo:
                        menu_funcionario(novo)

        elif tipo == "C":
            cpf = input("Digite seu CPF: ").strip()
            cliente = Cliente.verificar_cliente(cpf)
            if cliente:
                print(f"Cliente {cliente.nome} autenticado com sucesso!\n")
                menu_cliente(cliente)
            else:
                print("Cliente não encontrado.")
                opcao = input("Deseja se cadastrar como cliente? (S/N): ").strip().upper()
                if opcao == "S":
                    novo = Cliente.cadastrar_cliente()
                    if novo:
                        menu_cliente(novo)
        else:
            print("Opção inválida. Digite G, F, C ou S.")

def menu_gerente(gerente: Gerente):
    # Menu exclusivo do gerente — chama métodos da classe Gerente.
    while True:
        print("\nMenu do Gerente:")
        print("1. Adicionar Carro")
        print("2. Visualizar Funcionários")
        print("3. Visualizar Carros Vendidos")
        print("4. Voltar (logout)")

        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            gerente.adicionar_carro()
        elif opcao == "2":
            gerente.ver_historico_funcionarios()
        elif opcao == "3":
            gerente.ver_historico_carros_vendidos()
        elif opcao == "4":
            print("Logout gerente.")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_funcionario(funcionario):
    while True:
        print("\nMenu do Funcionário:")
        print("1. Visualizar Meus Dados")
        print("2. Alugar Carro")
        print("3. Voltar (logout)")

        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            # Visualiza os dados do funcionário
            funcionario.exibir_dados()
        elif escolha == "2":
            # Alugar carro
            modelo = input("Digite o modelo do carro que deseja alugar: ").strip()
            funcionario.alugarr_carro(modelo)
        elif escolha == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_cliente(cliente: Cliente):
    # Menu do cliente — usa métodos de Cliente.
    while True:
        print("\nMenu do Cliente:")
        print("1. Visualizar Carros Disponíveis")
        print("2. Comprar Carro")
        print("3. Voltar (logout)")

        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            cliente.visualizar_carros_disponiveis()
        elif opcao == "2":
            modelo = input("Digite o modelo do carro que deseja comprar: ").strip()
            cliente.comprar_carro(modelo)
        elif opcao == "3":
            print("Logout cliente.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    login()
