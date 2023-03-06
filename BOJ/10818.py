from sys import stdin, stdout

input = stdin.readline
output = stdout.write


N = int(input())
arr = list(map(int,input().split()))


print(min(arr), max(arr))