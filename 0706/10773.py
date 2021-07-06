#10773 제로 

num = int(input())
lis = [] 
sum = 0 

for _ in range(num):
    n = int(input())
    if n !=0 : lis.append(n)
    else : 
        if len(lis) == 0: lis.append(0)
        else:
            lis.pop()

for x in lis:
    sum +=x

print(sum)


