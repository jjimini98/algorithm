from sys import stdin

input = stdin.readline

N = int(input())
sik = input().rstrip()
ss = ''
nums = [ int(input()) for _ in range(N)]

answer = [] 
op = ["+","-","*","/"]
for i in sik:
    if i in op:
        
    else:
        answer.append(i)
