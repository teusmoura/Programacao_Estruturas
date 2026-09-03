import heapq

precos = [39.90, 249.90, 899.90, 24.90, 1299.90]
print(heapq.nsmallest(2, precos))
print(heapq.nlargest(2, precos))
