from database import criar_conexao

# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao = criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor = conexao.cursor()

cursor.execute("SELECT sku, nome, preco FROM produtos")
produtos = cursor.fetchall()
procurado = "MAQ-ROS-001"
for comparacoes, produto in enumerate(produtos, start=1):
    if produto[0] == procurado:
        print(produto, "| comparações:", comparacoes)
        break

cursor.close()
conexao.close()
