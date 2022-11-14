import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

for n in range(1,N+1):
    print("*"* n)
    print("\n")