from database import criar_conexao

# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao = criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor = conexao.cursor()

cursor.execute("""
    SELECT status, observacao, data_evento
    FROM historico_status_pedido
    WHERE id_pedido = 1
    ORDER BY data_evento
""")
pilha = cursor.fetchall()
print("Topo:", pilha[-1])
while pilha:
    print("pop ->", pilha.pop())

cursor.close()
conexao.close()
