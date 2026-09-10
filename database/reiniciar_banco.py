from pathlib import Path
import mysql.connector

try:
    from .config import get_mysql_config
except ImportError:
    from config import get_mysql_config

PASTA = Path(__file__).resolve().parent


def executar_arquivo(cursor, caminho):
    texto = Path(caminho).read_text(encoding="utf-8")
    for comando in texto.split(";"):
        comando = comando.strip()
        if comando:
            cursor.execute(comando)


conexao = mysql.connector.connect(**get_mysql_config(incluir_banco=False))
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
