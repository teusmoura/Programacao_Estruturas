from collections import deque

grafo = {1:[2,3],2:[1,5],3:[1,4],4:[3],5:[2]}
fila = deque([1]); distancia = {1:0}
while fila:
    atual = fila.popleft()
    for v in grafo.get(atual, []):
        if v not in distancia:
            distancia[v] = distancia[atual] + 1
            fila.append(v)
print(distancia)
