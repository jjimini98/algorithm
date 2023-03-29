from math import gcd

def solution(num):      
    answer =  min(num)
    for n in num:
        answer = n * answer // gcd(n, answer)

    return answer



if __name__ == '__main__': 
    arr = [6,8,14]
    # arr = [1,2,3]
    print(solution(arr))