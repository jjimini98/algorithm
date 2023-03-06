from sys import stdin, stdout

input = stdin.readline
output = stdout.write


N = int(input())
arr = list(map(int,input().split()))
arr.sort()


M = arr[-1]
new_arr = [] 

for n in range(N) :
    score = arr[n] / M *100 
    new_arr.append(score)


print(sum(new_arr)/N)