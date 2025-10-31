import json
import os

CARROS_FILE = "carros.json"
CARROS_VENDIDOS_FILE = "carros_vendidos.json"
CARROS_ALUGADOS_FILE = "carros_alugados.json" 

class Carro:
    def __init__(self, modelo, ano, preco):
        self.modelo = modelo
        self.ano = ano
        self.preco = preco

    @staticmethod
    def _read_json(path):
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    @staticmethod
    def _write_json(path, data):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def listar_carros():
        return Carro._read_json(CARROS_FILE)

    @staticmethod
    def adicionar_carro(modelo, ano, preco):
        carros = Carro.listar_carros()
        carros.append({"modelo": modelo, "ano": ano, "preco": preco, "status": "disponível", "comprador_nome": None, "comprador_cpf": None})
        Carro._write_json(CARROS_FILE, carros)
        print(f"Carro {modelo} adicionado com sucesso!")

    @staticmethod
    def listar_carros_vendidos():
        return Carro._read_json(CARROS_VENDIDOS_FILE)

    @staticmethod
    def listar_carros_alugados():
        return Carro._read_json(CARROS_ALUGADOS_FILE)

    @staticmethod
    def vender_carro(modelo, comprador_nome=None, comprador_cpf=None):
        carros = Carro.listar_carros()
        alvo = None
        for c in carros:
            if c["modelo"].lower() == modelo.lower():
                alvo = c
                break

        if not alvo:
            return False

        carros.remove(alvo)
        Carro._write_json(CARROS_FILE, carros)

        vendidos = Carro.listar_carros_vendidos()
        vendidos.append({
            "modelo": alvo["modelo"],
            "ano": alvo["ano"],
            "preco": alvo["preco"],
            "comprador_nome": comprador_nome,
            "comprador_cpf": comprador_cpf
        })
        Carro._write_json(CARROS_VENDIDOS_FILE, vendidos)
        return True

    @staticmethod
    def alugar_carro(modelo, comprador_nome=None, comprador_cpf=None):

        carros = Carro.listar_carros()
        alvo = None
        for c in carros:
            if c["modelo"].lower() == modelo.lower() and c["status"] == "disponível":
                alvo = c
                break

        if not alvo:
            return False  

        alvo["status"] = "alugado"
        alvo["comprador_nome"] = comprador_nome
        alvo["comprador_cpf"] = comprador_cpf
        Carro._write_json(CARROS_FILE, carros)

        alugados = Carro.listar_carros_alugados()
        alugados.append({
            "modelo": alvo["modelo"],
            "ano": alvo["ano"],
            "preco": alvo["preco"],
            "comprador_nome": comprador_nome,
            "comprador_cpf": comprador_cpf
        })
        Carro._write_json(CARROS_ALUGADOS_FILE, alugados)
        return True