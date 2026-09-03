from database import criar_conexao

class No:
    def __init__(self, chave, dado):
        self.chave = chave; self.dado = dado; self.esquerda = None; self.direita = None

def inserir(no, chave, dado):
    if no is None: return No(chave, dado)
    if chave < no.chave: no.esquerda = inserir(no.esquerda, chave, dado)
    else: no.direita = inserir(no.direita, chave, dado)
    return no

conexao = criar_conexao(); cursor = conexao.cursor()
cursor.execute("SELECT preco, sku, nome FROM produtos WHERE id_produto <= 8")
raiz = None
for preco, sku, nome in cursor.fetchall():
    raiz = inserir(raiz, preco, (sku, nome))
print("Raiz criada com preço:", raiz.chave, raiz.dado)
cursor.close(); conexao.close()
