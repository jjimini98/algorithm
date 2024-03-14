from sys import stdin
from collections import deque
input = stdin.readline


N, K = map(int, input().split())
kids = list(map(int,input().split()))

def divider(N,K,kids):
    kids = deque(kids[:-1])
    K -= 1
    situations = []

    for i in range(len(kids)-1): # 전체 학생
        tmp = []
        for cnt in range(K): # 나누는 기준 ? k = 3 3봉지 , K=2 면 2봉지
            tmp.append(kids[cnt])
            kids.popleft()
        situations.append(tmp)
    print(situations)

    # for sit in situations:
    #     for i in range()
    #     tmp = 0
    #     tmp += abs(sit[0][0][0] - sit[0][0][-1])
    #
    #     s_answer.append(tmp)
    # return min(tmp)
divider(N,K,kids)