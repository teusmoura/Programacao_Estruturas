grafo = {1:[2,3,5],2:[1,5],3:[1,4,6],4:[3,6],5:[1,2,6],6:[3,4,5]}
for vertice, vizinhos in grafo.items():
    print(vertice, "grau de saída:", len(vizinhos))
