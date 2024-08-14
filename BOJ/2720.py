from sys import stdin
input = stdin.readline


coins = [25, 10 , 5, 1]

for _ in range(int(input())):
  remain = int(input())
  result = []
  for coin in coins:
    val = remain // coin
    remain = remain % coin
    result.append(str(val))
  print(' '.join(result))