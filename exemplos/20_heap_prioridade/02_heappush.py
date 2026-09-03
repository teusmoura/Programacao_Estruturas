import heapq

heap = []
for prioridade, tarefa in [(3,"C"),(1,"A"),(2,"B")]:
    heapq.heappush(heap, (prioridade, tarefa))
while heap:
    print(heapq.heappop(heap))
