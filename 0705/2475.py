import sys

number = list(map(int, sys.stdin.readline().split(" ")))

sum = 0 
for x in number:
   sum += x**2 


print(sum%10)
