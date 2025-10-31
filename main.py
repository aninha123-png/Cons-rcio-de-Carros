import json
from gerente import Gerente
from funcionario import Funcionario
from cliente import Cliente
from carro import Carro

def identificar_tipo_usuario(cpf: str):

    if Gerente.verificar_gerente(cpf):
        return 'gerente'
    
    if Funcionario.verificar_funcionario(cpf):
        return 'funcionario'
    
    if Cliente.verificar_cliente(cpf):
        return 'cliente'
    
    return None

def login():
    while True:
        print("\n--- SISTEMA DE LOGIN ---")
        cpf = input("Digite seu CPF (ou 'S' para sair): ").strip()
        
        if cpf.upper() == "S":
            print("Saindo do sistema.")
            break
        
        if not cpf:
            print("CPF não pode estar vazio.")
            continue
        
        tipo_usuario = identificar_tipo_usuario(cpf)
        
        if tipo_usuario is None:
            print("Usuário não cadastrado.")
            opcao = input("Deseja se cadastrar? (S/N): ").strip().upper()
            if opcao == "S":
                cadastrar_usuario(cpf)
            continue
        
        senha = input("Digite sua senha: ").strip()
        
        if tipo_usuario == 'gerente':
            usuario = Gerente.verificar_gerente(cpf)
            if usuario and usuario.verificar_senha(senha):
                print(f"Gerente {usuario.nome} autenticado com sucesso!")
                menu_gerente(usuario)
            else:
                print("Senha incorreta.")
                
        elif tipo_usuario == 'funcionario':
            usuario = Funcionario.verificar_funcionario(cpf)
            if usuario and usuario.verificar_senha(senha):
                print(f"Funcionário {usuario.nome} autenticado com sucesso!")
                menu_funcionario(usuario)
            else:
                print("Senha incorreta.")
                
        elif tipo_usuario == 'cliente':
            usuario = Cliente.verificar_cliente(cpf)
            if usuario and usuario.verificar_senha(senha):
                print(f"Cliente {usuario.nome} autenticado com sucesso!")
                menu_cliente(usuario)
            else:
                print("Senha incorreta.")

def cadastrar_usuario(cpf: str):
    print("\n---CADASTRO DE USUÁRIO ---")
    print("1. Cliente")
    print("2. Funcionário")
    print("3. Gerente")
    
    opcao = input("Escolha o tipo de cadastro: ").strip()
    
    if opcao == "1":
        Cliente.cadastrar_cliente(cpf)
    elif opcao == "2":
        Funcionario.cadastrar_funcionario(cpf)
    elif opcao == "3":
        Gerente.cadastrar_gerente(cpf)
    else:
        print("Opção inválida.")

def menu_gerente(gerente: Gerente):
    while True:
        print("\nMenu do Gerente:")
        print("1. Adicionar Carro")
        print("2. Visualizar Funcionários")
        print("3. Visualizar Carros Vendidos")
        print("4. Visualizar Carros Alugados")
        print("5. Voltar (logout)")

        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            gerente.adicionar_carro()
        elif opcao == "2":
            gerente.ver_historico_funcionarios()
        elif opcao == "3":
            gerente.ver_historico_carros_vendidos()
        elif opcao == "4":
            gerente.ver_carros_alugados()
        elif opcao == "5":
            print("Logout gerente.")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_funcionario(funcionario):
    while True:
        print("\nMenu do Funcionário:")
        print("1. Visualizar Meus Dados")
        print("2. Visualizar Carros Disponíveis")
        print("3. Alugar Carro")
        print("4. Voltar (logout)")

        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            funcionario.exibir_dados()
        elif escolha == "2":
            Funcionario.visualizar_carros_disponiveis()
        elif escolha == "3":
            modelo = input("Digite o modelo do carro que deseja alugar: ").strip()
            funcionario.alugarr_carro(modelo)
        elif escolha == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_cliente(cliente: Cliente):
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