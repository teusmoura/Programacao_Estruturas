from database import criar_conexao

# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao = criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor = conexao.cursor()

cursor.execute("SELECT sku, nome, preco FROM produtos")
memoria = sorted(cursor.fetchall(), key=lambda p: p[2], reverse=True)
cursor.execute("SELECT sku, nome, preco FROM produtos ORDER BY preco DESC")
banco = cursor.fetchall()
print("Mesmo primeiro item?", memoria[0] == banco[0])
print(memoria[0])

cursor.close()
conexao.close()
