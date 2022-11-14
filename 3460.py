from sys import stdin, stdout

input = stdin.readline
output = stdout.write


for _ in range(int(input())):
    n = int(input())
    binn = bin(n)[::-1]
    for x in range(len(binn)):
        if binn[x] == "1":
            print(x, end= " ")
