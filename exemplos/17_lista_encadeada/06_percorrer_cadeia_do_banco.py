from database import criar_conexao
conexao=criar_conexao(); cursor=conexao.cursor()
cursor.execute("SELECT id_etapa,nome,id_proxima_etapa FROM etapas_reposicao")
etapas={id_etapa:(nome,prox) for id_etapa,nome,prox in cursor.fetchall()}
atual=1
while atual is not None:
    nome,atual=etapas[atual]
    print(nome)
cursor.close(); conexao.close()
