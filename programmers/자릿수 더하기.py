def solution(n):
    SN = str(n)
    answer = 0 
    for i in SN:
        answer += int(i)

    return answer 


if __name__ == "__main__":
    n = 987 
    print(solution(n))
