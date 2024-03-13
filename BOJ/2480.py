from sys import stdin

input = stdin.readline

# 방법 1 
# one, two, three = map(int, input().split())
# reward = 0 
# lis = [] 

# if one == two == three : 
#     reward += 10000 + (one * 1000)

# elif one == two or two == three : 
#     reward += 1000 + (two * 100)

# elif one == three : 
#     reward += 1000 + (one * 100)

# else: 
#     lis.append(one)
#     lis.append(two)
#     lis.append(three)
#     reward += max(lis) * 100

# print(reward)

# 방법 2
lis = list(map(int, input().split()))
reward = 0 
if lis[0] == lis[1] == lis[2]:
    reward += 10000 + (lis[0] * 1000)
elif lis[0] == lis[1] or lis[1] == lis[2] : 
    reward += 1000 + (lis[1] * 100)

elif lis[0] == lis[2]: 
    reward += 1000 + (lis[0] * 100)

else: 
    reward += max(lis) *100 

print(reward)