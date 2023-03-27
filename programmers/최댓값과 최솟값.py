def solution(s):

    lis = list(map(int, s.split()))
    return str(min(lis)) + " " + str(max(lis))





if __name__ == '__main__': 
    s = "1 2 3 4"
    print(solution(s))
