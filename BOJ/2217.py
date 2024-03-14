# from sys import stdin
#
# input = stdin.readline
#
# N = int(input())
#
# rope = sorted([int(input()) for _ in range(N)],reverse=True)
#
# answer = []
#
# if N > 2:
#     for x in range(1,(N+1)//2+1):
#         answer.append(rope[:x][-1] * x)
#
# else:
#     for x in range(1,N+1):
#         answer.append(rope[:x][-1] * x)
#
#
# print(answer[-1])



from sys import stdin
from itertools import combinations

input = stdin.readline

N = int(input())
rope = sorted([int(input()) for _ in range(N)])
answer = set()

for i in range(1,N+1):




    for combi in combinations(rope,i):
        answer.add(combi[0]*i)


print(max(answer))