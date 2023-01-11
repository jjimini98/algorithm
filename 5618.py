from sys import stdin, stdout

input = stdin.readline 
print = stdout.write

N = int(input())
nums = list(map(int, input().split()))
max_common = 0 
common = [] 

for x in range(min(nums), 0 , -1):
    if N == 2 :
        if nums[0] % x == 0 and nums[1] % x == 0 :
            max_common = x 
            break 
    
    if N == 3: 
        if nums[0] % x == 0 and  nums[1] % x == 0  and nums[2] % x == 0 : 
            max_common = x 
            break 
    
for c in range(max_common, 0, -1):
    if max_common % c == 0 :
        common.append(c)

for i in sorted(common):
    print(i)
