from sys import stdin

input = stdin.readline

N = int(input())
answer = [] 


for x in range(1,N):
    place_value = list(map(int, str(x)))
    if x + sum(place_value) == N : 
        answer.append(x)

if len(answer) == 0 :
    print(0)
else: 
    print(min(answer))