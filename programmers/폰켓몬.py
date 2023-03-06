# 시간초과
# from itertools import combinations
# def solution(nums):
#     answer = 0 
#     for x in combinations(nums,len(nums)//2):
#         # print(
#         answer = max(len(set(x)),answer)
#     print(answer)

def solution(nums):
    answer = set(nums)
    standard = len(nums) // 2 
    if standard < len(answer):
        return standard
    else: 
        return len(answer)

if __name__ == '__main__': 
    nums = [3,1,2,3]
    solution(nums)