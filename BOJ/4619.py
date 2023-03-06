from sys import stdin

input = stdin.readline

while True:
    B, N = map(int, input().split())
    dis = 999999
    answer = 0
    if B == N == 0 :
        break 
    
    elif B == 1: 
        print(1)
        continue

    elif N == 1 :
        print(B)
        continue

    for A in range(1,B//2+1):
        if abs(B-A**N) < dis: 
            dis = abs(B-A**N)
            answer = A

    print(answer)