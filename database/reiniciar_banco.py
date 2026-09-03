from pathlib import Path
import mysql.connector

PASTA = Path(__file__).resolve().parent


def executar_arquivo(cursor, caminho):
    texto = Path(caminho).read_text(encoding="utf-8")
    for comando in texto.split(";"):
        comando = comando.strip()
        if comando:
            cursor.execute(comando)


conexao = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
)
cursor = conexao.cursor()

try:
    cursor.execute("DROP DATABASE IF EXISTS lojas_rede")
    executar_arquivo(cursor, PASTA / "schema.sql")
    executar_arquivo(cursor, PASTA / "dados_iniciais.sql")
    conexao.commit()
    print("Banco lojas_rede reiniciado para o estado didático inicial.")
finally:
    cursor.close()
    conexao.close()
