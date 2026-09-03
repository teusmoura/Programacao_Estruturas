from database import criar_conexao

conexao = criar_conexao()
cursor = conexao.cursor()
try:
    cursor.execute("SELECT id_produto, nome FROM produtos LIMIT 3")
    for produto in cursor.fetchall():
        print(produto)
finally:
    cursor.close()
    conexao.close()
    print("Cursor e conexão foram fechados.")
