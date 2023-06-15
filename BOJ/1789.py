from sys import stdin

input = stdin.readline


N = int(input())
total = 0
i = 1

while True:
    if total > N:
        print(i-2)
        break
    elif total == N:
        print(i-1)
        break

    total += i
    i += 1

# print(i-2)
