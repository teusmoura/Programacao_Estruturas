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

### Recriar o ambiente virtual

Se o `.venv` estiver corrompido ou desatualizado, apague-o e rode `preparar_ambiente.cmd` novamente.

No PowerShell:

```powershell
Remove-Item -Recurse -Force .venv
.\preparar_ambiente.cmd
```

No Prompt de Comando (cmd.exe):

```bat
rmdir /s /q .venv
preparar_ambiente.cmd
```

Depois de recriar o `.venv`, execute novamente `python database\criar_banco.py` para recriar o banco `lojas_rede`.

### Limpar cache do Python

Para remover os arquivos `__pycache__` e `.pyc` gerados durante a execução:

No PowerShell:

```powershell
Get-ChildItem -Recurse -Directory -Filter __pycache__ | Remove-Item -Recurse -Force
Get-ChildItem -Recurse -Filter *.pyc | Remove-Item -Force
```

No Prompt de Comando (cmd.exe):

```bat
for /d /r %d in (__pycache__) do @rmdir /s /q "%d"
del /s /q *.pyc
```
