from database import criar_conexao
conexao=criar_conexao(); cursor=conexao.cursor()
def disponiveis(id_unidade):
    cursor.execute("SELECT id_produto FROM estoques WHERE id_unidade=%s AND quantidade>0",(id_unidade,))
    return {x[0] for x in cursor.fetchall()}
sete_lagoas=disponiveis(1); bh=disponiveis(2)
print("Produtos disponíveis nas duas unidades:",sete_lagoas & bh)
print("Somente em Sete Lagoas:",sete_lagoas-bh)
cursor.close(); conexao.close()
