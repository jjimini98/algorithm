from sys import stdin, stdout

input = stdin.readline
output = stdout.write


N = int(input())

def factorial(n) -> int:
    if n == 0 or n == 1:
        return 1 
    return n * factorial(n-1)

print(factorial(N))