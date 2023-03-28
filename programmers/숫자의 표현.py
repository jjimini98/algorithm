# 시간초과 
# def solution(n):

#     nums = [x for x in range(1,n)]
#     cumsum = []

#     for i in range(2, n):
#         for j in range(len(nums)):
#                 cs = sum(nums[j : j+i])
#                 if cs > n :
#                     break 
#                 else: 
#                     cumsum.append(cs)
#                 # cumsum.append(sum(nums[j : j+i]))

#     return cumsum.count(n) + 1



def solution(n):
    count = 1                 
    for i in range(1, n):        
        sumN = 0                     
        for j in range(i, n):  
            sumN += j               
            if sumN == n:           
                count += 1          
                break
            if sumN > n:           
                break
    return count


 
if __name__ == '__main__': 

    n = 15
    print(solution(n))
