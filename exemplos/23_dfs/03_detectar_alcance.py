grafo = {1:[2],2:[3],3:[],4:[5],5:[]}

def alcanca(origem, destino):
    pilha=[origem]; visitados=set()
    while pilha:
        atual=pilha.pop()
        if atual==destino: return True
        if atual in visitados: continue
        visitados.add(atual); pilha.extend(grafo.get(atual, []))
    return False

print(alcanca(1,3), alcanca(1,5))
