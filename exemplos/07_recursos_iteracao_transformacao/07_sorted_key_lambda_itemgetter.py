from operator import itemgetter

produtos = [
    (1, "Shampoo Nutritivo 350 ml", 39.90),
    (4, "Perfume Floral 100 ml", 249.90),
    (14, "Base Liquida Bege 30 ml", 899.90),
]
print(sorted(produtos, key=lambda p: p[2], reverse=True))
print(sorted(produtos, key=itemgetter(1)))
