import json
import os
from carro import Carro 
FUNCIONARIOS_FILE = "funcionarios.json"

class Funcionario:
    def __init__(self, nome: str, idade: int, salario: float, cpf: str, senha: str, cargo: str = "Funcionário"):
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.cpf = cpf
        self.senha = senha
        self.cargo = cargo

    def exibir_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Salário: R${self.salario:.2f}, CPF: {self.cpf}, Cargo: {self.cargo}")

    @staticmethod
    def _read_json():
        if os.path.exists(FUNCIONARIOS_FILE):
            with open(FUNCIONARIOS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    @staticmethod
    def listar_funcionarios():
        return Funcionario._read_json()  
    @staticmethod
    def verificar_funcionario(cpf: str):
        funcionarios = Funcionario.listar_funcionarios()  # Chama o método de listar funcionários
        for f in funcionarios:
            if f.get("cpf") == cpf:  
                return Funcionario(f["nome"], f["idade"], f["salario"], f["cpf"], f["senha"], f.get("cargo", "Funcionário"))
        return None  

    @staticmethod
    def cadastrar_funcionario(cpf: str):
        nome = input("Digite seu nome: ").strip()
        idade = int(input("Digite sua idade: ").strip())
        salario = float(input("Digite seu salário: ").strip())
        senha = input("Digite sua senha: ").strip()

        funcionarios = Funcionario.listar_funcionarios()

        for f in funcionarios:
            if f.get("cpf") == cpf:
                print("CPF já cadastrado como funcionário.")
                return None

        novo_funcionario = {
            "nome": nome, 
            "idade": idade, 
            "salario": salario, 
            "cpf": cpf, 
            "senha": senha,
            "cargo": "Funcionário"
        }
        funcionarios.append(novo_funcionario)

        with open(FUNCIONARIOS_FILE, "w", encoding="utf-8") as f:
            json.dump(funcionarios, f, indent=4)

        print(f"Funcionário {nome} cadastrado com sucesso!")
        return Funcionario(nome, idade, salario, cpf, senha)

    def verificar_senha(self, senha: str) -> bool:
        return self.senha == senha

    def alugarr_carro(self, modelo: str):
        sucesso = Carro.alugar_carro(modelo, comprador_nome=self.nome, comprador_cpf=self.cpf)
        if sucesso:
            print(f"Carro {modelo} alugado com sucesso!")
        else:
            print(f"Carro {modelo} não pode ser alugado.")

    @staticmethod
    def visualizar_carros_disponiveis():
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
        qtd_alugados = Carro.listar_carros_alugados()  
        print(f"Quantidade de carros alugados: {qtd_alugados}")