# queue를 활용한 풀이 
from sys import stdin
from collections import deque

input = stdin.readline

for _ in range(int(input())):
    N , M = map(int,input().split())
    nums = list(map(int,input().split()))
    answer = (M+1 , nums[M])
    answer_q = [] 
    queue = deque([])

    for idx , num in enumerate(nums):
        queue.append((idx+1, num))
    
    while queue:
        item = queue.popleft()
        if max(nums) == item[1]:
            nums.remove(max(nums))
            answer_q.append(item)
        else:
            queue.append(item)


    print(answer_q.index(answer)+1)   



# 우선순위 큐 (미완성)
# from sys import stdin
# from queue import PriorityQueue

# input = stdin.readline


# for _ in range(int(input())):
#     N, M = map(int,input().split())
#     nums = list(map(int,input().split()))
#     q = PriorityQueue()
#     answer = []


#     for idx, n in enumerate(nums):
#         q.put((-n,idx+1))



    # nums[0] 이랑 q의 0 번째가 다르면  다시 뒤에 put

    # for x in range(N):
    #     n, idx = q.get()
    #     print(n, idx)
        # if idx == M+1:
        #     print(idx)
    
    