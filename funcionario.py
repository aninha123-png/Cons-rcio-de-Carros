import json
import os
from carro import Carro  # Importando a classe Carro para poder usá-la

FUNCIONARIOS_FILE = "funcionarios.json"

class Funcionario:
    def __init__(self, nome: str, idade: int, salario: float, cpf: str, cargo: str = "Funcionário"):
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.cpf = cpf
        self.cargo = cargo

    def exibir_dados(self):
        """Exibe os dados do funcionário."""
        print(f"Nome: {self.nome}, Idade: {self.idade}, Salário: R${self.salario:.2f}, CPF: {self.cpf}, Cargo: {self.cargo}")

    @staticmethod
    def _read_json():
        #Lê o conteúdo do arquivo JSON e retorna os dados ou uma lista vazia em caso de erro.
        if os.path.exists(FUNCIONARIOS_FILE):
            with open(FUNCIONARIOS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    @staticmethod
    def listar_funcionarios():
        #Retorna a lista de funcionários (dicionários).#
        return Funcionario._read_json()  # Chama o método de leitura do arquivo JSON

    @staticmethod
    def verificar_funcionario(cpf: str):
        """Verifica se existe um funcionário com o CPF fornecido e retorna o funcionário, caso exista."""
        funcionarios = Funcionario.listar_funcionarios()  # Chama o método de listar funcionários
        for f in funcionarios:
            if f.get("cpf") == cpf:  # Verifica se o CPF corresponde
                return Funcionario(f["nome"], f["idade"], f["salario"], f["cpf"], f.get("cargo", "Funcionário"))
        return None  # Retorna None se não encontrar o funcionário

    @staticmethod
    def cadastrar_funcionario():
        #Cadastra um novo funcionário.
        nome = input("Digite seu nome: ").strip()
        idade = int(input("Digite sua idade: ").strip())
        salario = float(input("Digite seu salário: ").strip())
        cpf = input("Digite seu CPF: ").strip()

        funcionarios = Funcionario.listar_funcionarios()

        # Verifica se o CPF já existe
        for f in funcionarios:
            if f.get("cpf") == cpf:
                print("CPF já cadastrado como funcionário.")
                return None

        # Cria um novo funcionário
        novo_funcionario = {"nome": nome, "idade": idade, "salario": salario, "cpf": cpf, "cargo": "Funcionário"}
        funcionarios.append(novo_funcionario)

        # Escreve os dados do funcionário no arquivo JSON
        with open(FUNCIONARIOS_FILE, "w", encoding="utf-8") as f:
            json.dump(funcionarios, f, indent=4)

        print(f"Funcionário {nome} cadastrado com sucesso!")
        return Funcionario(nome, idade, salario, cpf)

    def alugarr_carro(self, modelo: str):
        #Aluga um carro (chama Carro.alugar_carro).
        sucesso = Carro.alugar_carro(modelo, comprador_nome=self.nome, comprador_cpf=self.cpf)
        if sucesso:
            print(f"Carro {modelo} alugado com sucesso!")
        else:
            print(f"Carro {modelo} não pode ser alugado.")

    @staticmethod
    def visualizar_carros_disponiveis():
        #Mostra os carros do estoque (chama Carro.listar_carros).
        carros = Carro.listar_carros()
        if not carros:
            print("Não há carros disponíveis para alugar.")
            return
        print("\nCarros disponíveis:")
        for c in carros:
            print(f"Modelo: {c['modelo']}, Ano: {c['ano']}, Preço: R${c['preco']:.2f}")
            print("-" * 30)

    @staticmethod
    def carros_alugados():
        """Exibe o número de carros alugados."""
        qtd_alugados = Carro.listar_carros_alugados()  # Verifique se esse método existe na classe Carro
        print(f"Quantidade de carros alugados: {qtd_alugados}")
