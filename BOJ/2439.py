from sys import stdin, stdout

input = stdin.readline
print = stdout.write


N = int(input())
for x in range(1,N+1):
    star = "*" * x
    print(star.rjust(N))
    print("\n")