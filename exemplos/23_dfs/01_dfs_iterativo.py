grafo = {1:[2,3],2:[1,5],3:[1,4],4:[3],5:[2]}
pilha = [1]; visitados = set()
while pilha:
    atual = pilha.pop()
    if atual in visitados: continue
    visitados.add(atual); print(atual)
    pilha.extend(reversed(grafo.get(atual, [])))
