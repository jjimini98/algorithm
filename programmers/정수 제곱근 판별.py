def solution(n):
    i = 1 
    answer = 0 
    while i <= n : 
        if i**2 == n : 
            answer = i + 1 
            break 
        i += 1 
    if answer == 0:  
        return -1 
    return answer**2 

if __name__ == "__main__":
    n = 3 
    print(solution(n))

