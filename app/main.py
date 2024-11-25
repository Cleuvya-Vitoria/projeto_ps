from fastapi import FastAPI, HTTPException
from app.models.despesa import Despesa
from app.services.csv_service import adicionar_no_csv, ler_do_csv, sobrescrever_csv
from app.services.zip_service import compactar_csv
from app.services.hash_service import calcular_hash_csv

app = FastAPI()


@app.get("/")
def home():
    return {"mensagem": "Bem-vindo à API de Compartilhamento de Despesas"}

@app.post("/despesas/")
def adicionar_despesa(despesa: Despesa):
    adicionar_no_csv(despesa)
    return {"mensagem": "Despesa adicionada com sucesso", "despesa": despesa}

@app.get("/despesas/")
def listar_despesas():
    despesas = ler_do_csv()
    if not despesas:
        return {"mensagem": "Nenhuma despesa encontrada"}
    return despesas

@app.put("/despesas/{id}")
def atualizar_despesa(id: int, despesa_atualizada: Despesa):
    despesas = ler_do_csv()
    atualizado = False
    for i, despesa in enumerate(despesas):
        if int(despesa["id"]) == id:
            despesas[i] = despesa_atualizada.dict()
            atualizado = True
            break
    if not atualizado:
        raise HTTPException(status_code=404, detail="Despesa não encontrada")
    sobrescrever_csv(despesas)
    return {"mensagem": "Despesa atualizada com sucesso", "despesa": despesa_atualizada}

@app.delete("/despesas/{id}")
def remover_despesa(id: int):
    despesas = ler_do_csv()
    despesas_filtradas = [d for d in despesas if int(d["id"]) != id]
    if len(despesas) == len(despesas_filtradas):
        raise HTTPException(status_code=404, detail="Despesa não encontrada")
    sobrescrever_csv(despesas_filtradas)
    return {"mensagem": "Despesa removida com sucesso"}

@app.get("/despesas/quantidade")
def contar_despesas():
    despesas = ler_do_csv()
    return {"quantidade": len(despesas)}

@app.get("/despesas/compactar")
def compactar_arquivo():
    nome_zip = compactar_csv()
    return {"mensagem": "Arquivo compactado com sucesso", "arquivo": nome_zip}

@app.get("/despesas/hash")
def hash_csv():
    valor_hash = calcular_hash_csv()
    if not valor_hash:
        raise HTTPException(status_code=404, detail="Arquivo CSV não encontrado")
    return {"hash": valor_hash}
