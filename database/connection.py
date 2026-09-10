import mysql.connector
from mysql.connector import MySQLConnection

from .config import get_mysql_config


def criar_conexao() -> MySQLConnection:
    """Cria uma conexão com o banco didático lojas_rede."""
    return mysql.connector.connect(**get_mysql_config("lojas_rede"))
