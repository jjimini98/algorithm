from sys import stdin
import heapq

input = stdin.readline

N = int(input())
heap = []

dasom = int(input())
purchase = dasom 

for _ in range(N-1):
    num = int(input())
    heapq.heappush(heap,-num)


if N == 1: 
    print(0)
else: 
    while True:
        if purchase > -min(heap):
            # print(-max(heap))
            break
        val = heapq.heappop(heap)
        heapq.heappush(heap, val+1)
        purchase += 1

    print(purchase-dasom)