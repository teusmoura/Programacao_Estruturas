from collections import deque

grafo = {1:[2,3],2:[1,5],3:[1,4],4:[3],5:[2]}
fila = deque([1])
visitados = {1}
while fila:
    atual = fila.popleft()
    print(atual)
    for vizinho in grafo.get(atual, []):
        if vizinho not in visitados:
            visitados.add(vizinho)
            fila.append(vizinho)
