from database import criar_conexao

# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao = criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor = conexao.cursor()
try:
    cursor.execute("SELECT id_produto, nome FROM produtos LIMIT 3")
    for produto in cursor.fetchall():
        print(produto)
finally:
    cursor.close()
    conexao.close()
    print("Cursor e conexão foram fechados.")
