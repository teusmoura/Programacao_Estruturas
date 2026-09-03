a = ["Shampoo", "Condicionador"]
b = a
b.append("Perfume")
print("a:", a)
print("b:", b)

c = a.copy()
c.append("Protetor Solar")
print("a após cópia:", a)
print("c:", c)

matriz = [[1, 2], [3, 4]]
copia = matriz.copy()
copia[0][0] = 999
print("Cópia rasa afeta lista interna compartilhada:", matriz)
