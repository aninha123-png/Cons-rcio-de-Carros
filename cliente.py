import json
import os
from carro import Carro

CLIENTES_FILE = "clientes.json"

class Cliente:
    def __init__(self, nome: str, idade: int, cpf: str, senha: str):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.senha = senha

    @staticmethod
    def _read_json(path: str):
        if not os.path.exists(path):
            return []
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    @staticmethod
    def _write_json(path: str, data: list):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def verificar_cliente(cpf: str):
        clientes = Cliente._read_json(CLIENTES_FILE)
        for c in clientes:
            if c.get("cpf") == cpf:
                return Cliente(c["nome"], c["idade"], c["cpf"], c["senha"])
        return None

    @staticmethod
    def cadastrar_cliente(cpf: str):
        cliente_nome = input("Digite seu nome: ").strip()
        cliente_idade = int(input("Digite sua idade: ").strip())
        cliente_senha = input("Digite sua senha: ").strip()

        clientes = Cliente._read_json(CLIENTES_FILE)

        for c in clientes:
            if c.get("cpf") == cpf:
                print("CPF já cadastrado como cliente.")
                return None

        novo_cliente = {
            "nome": cliente_nome, 
            "idade": cliente_idade, 
            "cpf": cpf, 
            "senha": cliente_senha
        }
        clientes.append(novo_cliente)

        Cliente._write_json(CLIENTES_FILE, clientes)
        print(f"Cliente {cliente_nome} cadastrado com sucesso!")
        return Cliente(cliente_nome, cliente_idade, cpf, cliente_senha)

    def verificar_senha(self, senha: str) -> bool:
        return self.senha == senha

    def visualizar_carros_disponiveis(self):
        carros = Carro.listar_carros()
        if not carros:
            print("Não há carros disponíveis.")
            return
        print("\nCarros disponíveis:")
        for c in carros:
            print(f"Modelo: {c['modelo']}, Ano: {c['ano']}, Preço: R${c['preco']:.2f}")
            print("-" * 30)

    def comprar_carro(self, modelo: str):
        sucesso = Carro.vender_carro(modelo, comprador_nome=self.nome, comprador_cpf=self.cpf)
        if sucesso:
            print(f"Compra do carro {modelo} realizada com sucesso!")
        else:
            print("Carro não encontrado ou já vendido.")