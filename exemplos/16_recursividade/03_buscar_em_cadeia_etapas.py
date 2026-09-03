etapas = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: None}

def percorrer(id_atual):
    if id_atual is None:
        return
    print(id_atual)
    percorrer(etapas[id_atual])

percorrer(1)
