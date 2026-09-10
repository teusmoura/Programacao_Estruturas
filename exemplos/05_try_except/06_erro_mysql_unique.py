import mysql.connector
from database import criar_conexao

# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao = criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
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
