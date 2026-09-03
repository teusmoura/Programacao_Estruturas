from database import criar_conexao

conexao = criar_conexao()
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
