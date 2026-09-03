grafo = {1:[2,3],2:[1,5],3:[1,4],4:[3],5:[2]}
visitados = set()

def dfs(atual):
    if atual in visitados: return
    visitados.add(atual); print(atual)
    for v in grafo.get(atual, []): dfs(v)

dfs(1)
