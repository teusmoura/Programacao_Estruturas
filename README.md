# Programação — Estruturas de Dados com Python e MySQL

Este pacote dá continuidade a Algoritmos e Lógica de Programação. Ele separa:

- `exemplos/`: códigos completos, pequenos e executáveis;
- `exercicios/`: arquivos `.py` contendo somente enunciados;
- `database/`: banco didático e rotinas de preparação/reinicialização.

## Cenário do banco

`lojas_rede` é uma **simplificação didática de uma grande rede varejista**, com lojas principalmente em Minas Gerais, algumas unidades fora do estado, centros de distribuição, cinco canais de venda e rotas logísticas. Foram mantidas somente as tabelas que dão sentido aos exemplos e atividades.

A mesma informação aparece de formas diferentes ao longo da disciplina: um registro retornado pelo MySQL vira `tuple`; vários registros viram uma `list` de tuplas; conjuntos comparam disponibilidade entre lojas; solicitações de reposição viram fila ou heap; categorias formam árvore; rotas formam grafo.

## Princípio central

**Memória não é persistência.** Modificar uma estrutura Python não altera automaticamente o banco. Para persistir uma mudança, é necessária uma operação SQL explícita e, quando aplicável, `commit()`.

## Preparação

1. Execute `preparar_ambiente.cmd`.
2. Ajuste a senha do MySQL nos arquivos de `database/`, se necessário.
3. Execute `python database\criar_banco.py`.
4. Use `python database\reiniciar_banco.py` quando precisar retornar aos dados iniciais.
