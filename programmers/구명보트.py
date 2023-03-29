# 시간초과 
# def solution(people, limit):
#     answer = 0
#     people.sort(reverse = True)
#     while people:

#         if people == [0] * len(people) : 
#             return answer
        
#         l = limit
#         for i in range(len(people)):
#             if people[i] != 0 and people[i] <= l :
#                 l -= people[i]
#                 people[i] = 0 

#         answer += 1

# 시간초과 
# def solution(people, limit):
#     answer = []
#     n = 0 
#     tmp = []
#     people.sort(reverse = True)
#     l = limit 

#     while True:

#         # 종료조건 
#         if people == [9999] * len(people):
#             return answer

#         if people[n] != 9999 and people[n] <= l:
#             l -= people[n]
#             tmp.append(people[n])
#             people[n] = 9999

        
#         if n < len(people)-1 :
#             n += 1
#         else :
#             n = 0 
#             answer.append(tmp)
#             l = limit
#             tmp = []

        # print(answer)


# 문제를 제대로 읽자.. 문제에서 최대 2명까지만 탈 수 있다고 했음
from collections import deque

def solution(people, limit):
    answer = 0
    p = sorted(people,reverse= True)
    p = deque(p)

    while len(p) > 1:
        
        if p[0] + p[-1] <= limit:
            p.popleft()
            p.pop()
            answer += 1 
        else:
            p.popleft()
            answer += 1
    
    if len(p) == 1:
        answer += 1

    return answer
    







if __name__ == '__main__': 
    # people = [100,50,40,50,70,20]
    people = [70,50,80]
    # people = [10,20,30,40,50]
    # people = [40,40,40,40,40]
    limit = 100
    print(solution(people,limit))