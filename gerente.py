from funcionario import Funcionario
from carro import Carro
import json

class Gerente(Funcionario):
    def __init__(self, nome: str, idade: int, salario: float, cpf: str, cargo: str = "Gerente"):
        super().__init__(nome, idade, salario, cpf, cargo)

    @staticmethod
    def verificar_gerente(cpf: str):
        # Verifica se existe um gerente (cargo == 'Gerente') com o CPF; retorna instância ou None.
        funcionarios = Funcionario.listar_funcionarios()
        for f in funcionarios:
            if f.get("cpf") == cpf and f.get("cargo", "").lower() == "gerente":
                return Gerente(f["nome"], f["idade"], f["salario"], f["cpf"], f.get("cargo", "Gerente"))
        return None

    @staticmethod
    def cadastrar_gerente():
        # Cadastra o gerente. Apenas permite um gerente no sistema (requisito).
        funcionarios = Funcionario.listar_funcionarios()
        # Verifica se já existe gerente
        for f in funcionarios:
            if f.get("cargo", "").lower() == "gerente":
                print("Já existe um gerente cadastrado. Não é permitido cadastrar outro.")
                return None

        nome = input("Digite seu nome: ").strip()
        idade = int(input("Digite sua idade: ").strip())
        salario = float(input("Digite seu salário: ").strip())
        cpf = input("Digite seu CPF: ").strip()

        # Verificar CPF já existe entre funcionários
        for f in funcionarios:
            if f.get("cpf") == cpf:
                print("CPF já cadastrado como funcionário/gerente.")
                return None

        novo = {"nome": nome, "idade": idade, "salario": salario, "cpf": cpf, "cargo": "Gerente"}
        funcionarios.append(novo)
        
        # Gravando as informações no arquivo JSON
        with open("funcionarios.json", "w", encoding="utf-8") as fh:
            json.dump(funcionarios, fh, indent=4, ensure_ascii=False)

        print(f"Gerente {nome} cadastrado com sucesso!")
        return Gerente(nome, idade, salario, cpf, "Gerente")

    # Métodos exclusivos do gerente (usa Carro e Funcionario)
    def adicionar_carro(self):
        # Solicita dados e adiciona um carro via Carro.adicionar_carro.
        modelo = input("Digite o modelo do carro: ").strip()
        ano = int(input("Digite o ano do carro: ").strip())
        preco = float(input("Digite o preço do carro: ").strip())
        Carro.adicionar_carro(modelo, ano, preco)

    def ver_historico_funcionarios(self):
        # Exibe todos os funcionários cadastrados.
        funcionarios = Funcionario.listar_funcionarios()
        if not funcionarios:
            print("Nenhum funcionário cadastrado.")
            return
        print("\nHistórico de Funcionários:")
        for f in funcionarios:
            print(f"Nome: {f['nome']}, Idade: {f['idade']}, Salário: R${f['salario']:.2f}, CPF: {f['cpf']}, Cargo: {f.get('cargo','Funcionário')}")
        print("-" * 40)

    def ver_historico_carros_vendidos(self):
        # Exibe o histórico de carros vendidos.
        vendidos = Carro.listar_carros_vendidos()
        if not vendidos:
            print("Nenhum carro vendido ainda.")
            return
        print("\nHistórico de Carros Vendidos:")
        for v in vendidos:
            comprador = v.get("comprador_nome") or "—"
            cpf = v.get("comprador_cpf") or "—"
            print(f"Modelo: {v['modelo']}, Ano: {v.get('ano')}, Preço: R${v['preco']:.2f}, Comprador: {comprador} ({cpf})")
        print("-" * 40)

    def ver_carros_alugados(self):
        # Exibe o histórico de carros alugados por funcionários.
        alugados = Carro.listar_carros_alugados()  # Agora pegamos o histórico de carros alugados
        if not alugados:
            print("Nenhum carro alugado ainda.")
            return
        print("\nCarros Alugados:")
        for v in alugados:
            comprador = v.get("comprador_nome") or "—"
            cpf = v.get("comprador_cpf") or "—"
            print(f"Modelo: {v['modelo']}, Ano: {v.get('ano')}, Preço: R${v['preco']:.2f}, Alugado por: {comprador} ({cpf})")
        print("-" * 40)
