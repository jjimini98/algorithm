from sys import stdin, stdout

input = stdin.readline
print = stdout.write

N = int(input())

for x in range(N, 0, -1):
    print((' '*(N-x) + "*" * (2*x-1) + ' '))
    print("\n")