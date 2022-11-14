from sys import stdin, stdout

input = stdin.readline
output = stdout.write


arr = [int(input()) for _ in range(7)]

odd_arr = [x for x in arr if x %2 != 0]


if len(odd_arr) != 0 : 
    print(sum(odd_arr))
    print(min(odd_arr))
else:
    print(-1)