from database import criar_conexao
# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao=criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor=conexao.cursor()
cursor.execute("SELECT id_unidade,nome FROM unidades"); nomes=dict(cursor.fetchall())
cursor.execute("SELECT id_origem,id_destino FROM rotas WHERE ativa=1")
for origem,destino in cursor.fetchall()[:8]: print(nomes[origem],"->",nomes[destino])
cursor.close(); conexao.close()
