from sys import stdin, stdout

input = stdin.readline
print = stdout.write

N = int(input())
standard = 2*N-1

for x in range(1, N+1):
    print((' '*(N-x) + "*" * (2*x-1) + ' '))
    print("\n")
