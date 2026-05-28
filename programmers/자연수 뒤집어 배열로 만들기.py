def solution(n):
    SN = str(n)
    
    answer = [int(i) for i in reversed(SN)]

    return answer 


if __name__ == "__main__":
    n = 12345
    print(solution(n))
     
