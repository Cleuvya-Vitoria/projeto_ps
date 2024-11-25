import hashlib

def calcular_hash_csv():
    try:
        with open("despesas.csv", mode="rb") as arquivo:
            conteudo = arquivo.read()
            return hashlib.sha256(conteudo).hexdigest()
    except FileNotFoundError:
        return None
