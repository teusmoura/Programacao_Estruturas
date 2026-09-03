from collections import deque

fila = deque(["Ana", "Bruno", "Carla"])
fila.append("Diego")
print("Atendido:", fila.popleft())
print(fila)
