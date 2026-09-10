from database import criar_conexao

# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao = criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor = conexao.cursor()

cursor.execute("SELECT id_historico, status FROM historico_status_pedido WHERE id_pedido=1 ORDER BY data_evento")
pilha = cursor.fetchall()
removido = pilha.pop()
print("Removido da pilha:", removido)
cursor.execute("SELECT COUNT(*) FROM historico_status_pedido WHERE id_pedido=1")
print("Registros continuam no banco:", cursor.fetchone()[0])

cursor.close()
conexao.close()
