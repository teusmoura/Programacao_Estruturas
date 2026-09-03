grafo = {}
arestas = [(1,2),(1,3),(2,1),(3,1)]
for origem, destino in arestas:
    grafo.setdefault(origem, set()).add(destino)
print(grafo)
