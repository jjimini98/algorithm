# 시간초과 
# def solution(n):
#     if n == 0:
#         return 0
#     if n == 1 :
#         return 1
#     return solution(n-1) + solution(n-2) % 1234567


# 리스트에 값을 계속 저장해두는 방식 사용 
def solution(n):
    num = 2
    lis = [0,1] + [0 for _ in range(n-2)]
    while num < n : 

        if lis[num] == 0 :
            lis[num] = (lis[num-2] + lis[num-1]) % 1234567

        num += 1 

    return (lis[num-2] + lis[num-1]) % 1234567

if __name__ == '__main__': 
    print(solution(5))
    # print(solution(2))
