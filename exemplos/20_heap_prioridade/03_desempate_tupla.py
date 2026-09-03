import heapq
from datetime import datetime
heap=[]
heapq.heappush(heap,(1,datetime(2026,8,29,10),1,"Repor perfume"))
heapq.heappush(heap,(1,datetime(2026,8,28,18),8,"Repor sabonete"))
print(heapq.heappop(heap))
