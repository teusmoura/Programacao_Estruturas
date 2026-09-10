from database import criar_conexao

# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao = criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor = conexao.cursor()
def skus_da_unidade(id_unidade):
    cursor.execute("""
        SELECT p.sku FROM estoques e
        JOIN produtos p ON p.id_produto=e.id_produto
        WHERE e.id_unidade=%s AND e.quantidade > 0
    """, (id_unidade,))
    return {linha[0] for linha in cursor.fetchall()}

sete_lagoas = skus_da_unidade(1)
bh = skus_da_unidade(2)
print("Em ambas:", sete_lagoas & bh)
print("Somente Sete Lagoas:", sete_lagoas - bh)
print("Em pelo menos uma:", sete_lagoas | bh)
cursor.close(); conexao.close()
