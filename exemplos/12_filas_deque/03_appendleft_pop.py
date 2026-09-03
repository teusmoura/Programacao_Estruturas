from collections import deque

dados = deque([2, 3])
dados.appendleft(1)
dados.append(4)
print(dados.popleft())
print(dados.pop())
