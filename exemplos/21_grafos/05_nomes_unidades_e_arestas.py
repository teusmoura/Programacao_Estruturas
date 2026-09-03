from database import criar_conexao
conexao=criar_conexao(); cursor=conexao.cursor()
cursor.execute("SELECT id_unidade,nome FROM unidades"); nomes=dict(cursor.fetchall())
cursor.execute("SELECT id_origem,id_destino FROM rotas WHERE ativa=1")
for origem,destino in cursor.fetchall()[:8]: print(nomes[origem],"->",nomes[destino])
cursor.close(); conexao.close()
