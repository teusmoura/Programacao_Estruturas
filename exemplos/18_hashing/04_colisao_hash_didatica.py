def hash_didatico(chave, tamanho):
    return sum(ord(c) for c in chave) % tamanho

for chave in ["ABC", "ACB", "XYZ"]:
    print(chave, "->", hash_didatico(chave, 5))
