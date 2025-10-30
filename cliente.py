import json
import os
from carro import Carro

CLIENTES_FILE = "clientes.json"

class Cliente:
    def __init__(self, nome: str, idade: int, cpf: str):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    @staticmethod
    def _read_json(path: str):
        #Lê o conteúdo do arquivo JSON e retorna os dados ou uma lista vazia em caso de erro.
        if not os.path.exists(path):
            return []
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    @staticmethod
    def _write_json(path: str, data: list):
        #Escreve os dados no arquivo JSON.
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def verificar_cliente(cpf: str):
        #Verifica se o cliente já existe com o CPF informado.
        clientes = Cliente._read_json(CLIENTES_FILE)
        for c in clientes:
            if c.get("cpf") == cpf:
                return Cliente(c["nome"], c["idade"], c["cpf"])
        return None

    @staticmethod
    def cadastrar_cliente():
        #Cadastra um novo cliente.
        cliente_nome = input("Digite seu nome: ").strip()
        cliente_idade = int(input("Digite sua idade: ").strip())
        cliente_cpf = input("Digite seu CPF: ").strip()

        clientes = Cliente._read_json(CLIENTES_FILE)

        # Verifica se o CPF já existe
        for c in clientes:
            if c.get("cpf") == cliente_cpf:
                print("CPF já cadastrado como cliente.")
                return None

        novo_cliente = {"nome": cliente_nome, "idade": cliente_idade, "cpf": cliente_cpf}
        clientes.append(novo_cliente)

        # Escreve os dados do cliente no arquivo JSON
        Cliente._write_json(CLIENTES_FILE, clientes)
        print(f"Cliente {cliente_nome} cadastrado com sucesso!")
        return Cliente(cliente_nome, cliente_idade, cliente_cpf)

    def visualizar_carros_disponiveis(self):
        # Mostra os carros do estoque (chama Carro.listar_carros).
        carros = Carro.listar_carros()
        if not carros:
            print("Não há carros disponíveis.")
            return
        print("\nCarros disponíveis:")
        for c in carros:
            print(f"Modelo: {c['modelo']}, Ano: {c['ano']}, Preço: R${c['preco']:.2f}")
            print("-" * 30)

    def comprar_carro(self, modelo: str):
        # Compra um carro (chama Carro.vender_carro).
        sucesso = Carro.vender_carro(modelo, comprador_nome=self.nome, comprador_cpf=self.cpf)
        if sucesso:
            print(f"Compra do carro {modelo} realizada com sucesso!")
        else:
            print("Carro não encontrado ou já vendido.")
