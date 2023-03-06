from sys import stdin
# 리스트 append , pop 하는데 시간이 많이 소요됨. dictionary로 이문제 해결 가능~ 

input = stdin.readline

n = int(input())

logs = dict()
staff = list() 

for _ in range(n):
    name , status = input().split()
    status = status.rstrip()

    logs[name] = status

for k,v in logs.items():
    if v == "enter": 
        staff.append(k)


staff.sort(reverse=True)

print(*staff , sep = "\n")