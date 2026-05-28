def solution(s): 
    if "+" in s: 
        return int(s[1:])
    else: 
        return int(s)




if __name__ == "__main__":
    number = input()
    print(solution(number))