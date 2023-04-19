from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())
origin = list(map(int,input().split()))
q = deque(origin)
new_q = deque([i for i in range(1,len(origin)+1)])
qq = [] 

while q:
    
    loop = q.popleft()
    n_loop = new_q.popleft()
    qq.append(str(n_loop))

    try: 
        if loop >= 0 : 

            for _ in range(loop-1):
                q.append(q.popleft())
                new_q.append(new_q.popleft())


        else: 
            for _ in range(abs(loop)):
                q.appendleft(q.pop())
                new_q.appendleft(new_q.pop())
    except:
        continue


print(' '.join(qq))
# answer = ''
    
# for x in new_q:
#     answer += str(origin.index(x)+1)
#     answer += ' '

# print(answer[:-1])