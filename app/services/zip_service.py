import zipfile

def compactar_csv():
    nome_zip = "despesas.zip"
    with zipfile.ZipFile(nome_zip, "w") as zipf:
        zipf.write("despesas.csv", arcname="despesas.csv")
    return nome_zip
