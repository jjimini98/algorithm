from sys import stdin, stdout
# from string import ascii_lowercase

input = stdin.readline
output = stdout.write


S = input().rstrip()


for alpha in "abcdefghijklmnopqrstuvwxyz":
    print(S.find(alpha), end=" ")