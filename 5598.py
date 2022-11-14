from sys import stdin, stdout
input = stdin.readline
output = stdout.write

caesar = input().rstrip()
answer = ''
before = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
after = ["D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C"]

for c in caesar:
    idx = after.index(c)
    answer += before[idx]


print(answer)