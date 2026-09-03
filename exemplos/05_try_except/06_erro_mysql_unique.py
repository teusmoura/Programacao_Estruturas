import mysql.connector
from database import criar_conexao

conexao = criar_conexao()
cursor = conexao.cursor()
try:
    cursor.execute("""
        INSERT INTO clientes (nome, cpf_cnpj, email)
        VALUES (%s, %s, %s)
    """, ("Duplicado", "111.111.111-01", "dup@email.com"))
    conexao.commit()
except mysql.connector.Error as erro:
    conexao.rollback()
    print("Erro do MySQL:", erro)
finally:
    cursor.close()
    conexao.close()
