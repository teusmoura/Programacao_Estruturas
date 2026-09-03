from database import criar_conexao

conexao = criar_conexao()
cursor = conexao.cursor()

cursor.execute("SELECT id_historico, status FROM historico_status_pedido WHERE id_pedido=1 ORDER BY data_evento")
pilha = cursor.fetchall()
removido = pilha.pop()
print("Removido da pilha:", removido)
cursor.execute("SELECT COUNT(*) FROM historico_status_pedido WHERE id_pedido=1")
print("Registros continuam no banco:", cursor.fetchone()[0])

cursor.close()
conexao.close()
