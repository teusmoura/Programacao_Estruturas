from bisect import bisect_left

valores = [10, 20, 30, 40, 50]
pos = bisect_left(valores, 30)
print(pos, valores[pos])
