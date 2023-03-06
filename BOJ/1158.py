# from collections import deque

# N , K = map(int, input().split())
# people = deque([i for i in range(1,N+1)])
# answer = []
# idx = 0 

# while True: 
#     if len(people) == 0: break
#     if idx == K:
#         omit = people.pop()
#         answer.append(str(omit))
#         idx = 0 

#     else: 
#         people.append(people.popleft())
#         idx += 1

# print("<" +', '.join(answer)+ ">")



from sys import stdin
from collections import deque

input = stdin.readline

N, K = map(int, input().split())
q = deque([x for x in range(1,N+1)])

answer = []

def rotation(q : deque) -> deque:
    if len(q) != 0 :
        item = q.popleft() 
        q.append(item)
    return q

while True:
    if len(q) == 0:
        break 

    for _ in range(K-1):
        rotation(q)
    
    answer.append(str(q.popleft()))

print( f"<{', '.join(answer)}>" )


