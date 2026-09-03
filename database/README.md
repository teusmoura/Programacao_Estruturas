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

1. Ajuste usuário/senha nos arquivos Python de `database/` se necessário.
2. Execute `python database/criar_banco.py` na primeira utilização.
3. Para restaurar o estado didático inicial, execute `python database/reiniciar_banco.py`.
