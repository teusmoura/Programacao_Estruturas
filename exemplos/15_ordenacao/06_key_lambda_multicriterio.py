produtos = [
    ("Shampoo", 39.90, 45),
    ("Perfume", 249.90, 24),
    ("Condicionador", 79.90, 32),
]
print(sorted(produtos, key=lambda p: p[1]))
print(sorted(produtos, key=lambda p: (-p[2], p[0])))
