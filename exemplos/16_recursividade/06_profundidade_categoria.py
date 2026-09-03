pais = {2: 1, 12: 2, 1: None}

def profundidade(id_categoria):
    pai = pais[id_categoria]
    if pai is None:
        return 0
    return 1 + profundidade(pai)

print(profundidade(12))
