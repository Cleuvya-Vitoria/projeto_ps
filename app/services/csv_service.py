import csv
from typing import List, Dict
from app.models.despesa import Despesa

ARQUIVO_CSV = "despesas.csv"
CAMPOS = ["id", "descricao", "valor", "status", "grupo_id", "data_criacao"]

def adicionar_no_csv(despesa: Despesa):
    with open(ARQUIVO_CSV, mode="a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=CAMPOS)
        escritor.writerow(despesa.dict())

def ler_do_csv() -> List[Dict]:
    try:
        with open(ARQUIVO_CSV, mode="r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            return [linha for linha in leitor]
    except FileNotFoundError:
        return []

def sobrescrever_csv(despesas: List[Dict]):
    with open(ARQUIVO_CSV, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=CAMPOS)
        escritor.writeheader()
        escritor.writerows(despesas)
