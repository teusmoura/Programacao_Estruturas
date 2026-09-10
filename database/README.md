# Banco didático `lojas_rede`

O banco representa **uma rede varejista fictícia simplificada**, com lojas principalmente em Minas Gerais, algumas unidades fora do estado, centros de distribuição, cinco canais de venda e rotas logísticas. Ele foi dimensionado somente para dar sentido aos exemplos e às atividades de Estruturas de Dados; não pretende reproduzir um ERP real.

## Entidades usadas na disciplina

- `clientes`, `fornecedores`, `produtos` e `categorias`: registros, coleções, busca, ordenação, hashing e árvores;
- `unidades` e `estoques`: lojas/CDs, disponibilidade por unidade, conjuntos e transações;
- `canais_venda`, `pedidos` e `itens_pedido`: consultas, agrupamentos, CRUD e transações;
- `historico_status_pedido`: pilha/histórico;
- `solicitacoes_reposicao`: FIFO com `deque` e fila de prioridade com `heapq`;
- `etapas_reposicao`: lista encadeada e recursividade;
- `rotas`: grafos, BFS e DFS.

## Regra central

Um `SELECT` materializa valores na memória. Alterar uma `list`, `dict`, `set`, `deque`, heap ou qualquer outra estrutura Python **não altera o MySQL**. Persistência exige SQL (`INSERT`, `UPDATE`, `DELETE`) e, quando aplicável, `commit()`.

## Preparação

No padrão XAMPP, use:

- Host: `localhost`
- Porta: `3306`
- Usuário: `root`
- Senha: vazia

1. Verifique se o MySQL do XAMPP está rodando.
2. Se o padrão foi alterado, ajuste as credenciais com variáveis de ambiente:

```powershell
$env:MYSQL_USER = "root"
$env:MYSQL_PASSWORD = "sua_senha"
$env:MYSQL_HOST = "localhost"
$env:MYSQL_PORT = "3306"
```

3. Execute `python database/criar_banco.py` na primeira utilização.
4. Para restaurar o estado didático inicial, execute `python database/reiniciar_banco.py`.
