from collections import deque

grafo = {1:[2,3],2:[1,5],3:[1,4],4:[3],5:[2]}
origem, destino = 1, 5
fila = deque([origem]); anterior = {origem: None}
while fila:
    atual = fila.popleft()
    if atual == destino: break
    for v in grafo.get(atual, []):
        if v not in anterior:
            anterior[v] = atual; fila.append(v)

caminho = []
atual = destino
while atual is not None:
    caminho.append(atual); atual = anterior[atual]
print(list(reversed(caminho)))
