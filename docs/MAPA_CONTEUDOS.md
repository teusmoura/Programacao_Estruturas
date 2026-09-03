# MAPA DE CONTEÚDOS

O banco `lojas_rede` é intencionalmente enxuto. Lojas e CDs são `unidades`; estoque é sempre por unidade; pedidos têm um canal principal; distribuição é representada por solicitações de reposição e rotas.

| Pasta | Conteúdo | Dados usados |
|---|---|---|
| `01_tuplas` | Tuplas e fetchone() | clientes, produtos |
| `02_listas` | Listas, slicing, cópias e fetchall() | produtos, estoques |
| `03_dicionarios` | Dicionários e transformação de registros | produtos, estoques |
| `04_sets` | Conjuntos e disponibilidade entre unidades | unidades, estoques, produtos |
| `05_try_except` | Tratamento de exceções | clientes, itens_pedido |
| `06_funcoes_parametro_retorno` | Funções aplicadas a coleções e consultas | clientes, produtos, estoques |
| `07_recursos_iteracao_transformacao` | enumerate, zip, comprehensions, any/all, agregações, key/lambda, Counter/defaultdict | pedidos, canais_venda, produtos |
| `08_crud_persistencia` | SELECT/INSERT/UPDATE/DELETE | clientes, produtos, pedidos |
| `09_transacoes` | commit, rollback, FOR UPDATE e atomicidade | estoques, pedidos, itens_pedido |
| `10_complexidade` | Crescimento e custo | produtos |
| `11_pilhas` | LIFO e histórico | historico_status_pedido |
| `12_filas_deque` | FIFO e deque | solicitacoes_reposicao |
| `13_busca_linear` | Busca sequencial | produtos |
| `14_busca_binaria` | Busca em coleção ordenada | produtos |
| `15_ordenacao` | Algoritmos e sorted/sort | produtos, estoques |
| `16_recursividade` | Caso base e hierarquias | categorias, etapas_reposicao |
| `17_lista_encadeada` | Nós e encadeamento | etapas_reposicao |
| `18_hashing` | dict/set e acesso por chave | produtos, clientes, estoques |
| `19_arvores` | Árvores, BST e percursos | categorias, produtos |
| `20_heap_prioridade` | heapq e fila de prioridade | solicitacoes_reposicao |
| `21_grafos` | Adjacência, matriz e pesos | unidades, rotas |
| `22_bfs` | Busca em largura | unidades, rotas |
| `23_dfs` | Busca em profundidade | unidades, rotas, categorias |
| `24_integracao` | Escolha e combinação de estruturas | banco completo |
