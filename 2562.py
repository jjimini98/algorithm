from sys import stdin, stdout

input = stdin.readline  
output = stdout.write


arr = [int(input()) for _ in range(9)] 

print(max(arr))
print(arr.index(max(arr))+1)