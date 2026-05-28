def solution(n):
    if n % 2 == 0: 
        return "Even"
    else: 
        return "Odd"
    

if __name__ == "__main__":
    n = 4
    print(solution(n))
    n = 0 
    print(solution(n))