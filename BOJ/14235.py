from sys import stdin
import heapq

input = stdin.readline

N = int(input())

gift = [] 

for _ in range(N):
    
    a = input()

    if a[0] == "0" :
        try : 
            here = heapq.heappop(gift)
            print(abs(here))
        except:
            print(-1)
    else:
        newgift = list(map(int, a.split()))[1:]
        for i in newgift:
            heapq.heappush(gift,-i)
