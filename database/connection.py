import mysql.connector
from mysql.connector import MySQLConnection


def criar_conexao() -> MySQLConnection:
    """Cria uma conexão com o banco didático lojas_rede."""
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="lojas_rede",
    )
