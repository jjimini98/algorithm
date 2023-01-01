from collections import deque

N , K = map(int, input().split())
people = deque([i for i in range(1,N+1)])
answer = []
idx = 0 

while True: 
    if len(people) == 0: break
    if idx == K:
        omit = people.pop()
        answer.append(str(omit))
        idx = 0 

    else: 
        people.append(people.popleft())
        idx += 1

print("<" +', '.join(answer)+ ">")