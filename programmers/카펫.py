def solution(brown, yellow):

    total = brown + yellow

    for v in range(1,total//2+1):

        if total % v == 0 :
            h = total // v 

            if (h-2) * (v-2) == yellow:
                return [h,v]




if __name__ == '__main__': 
    brown = 24
    yellow = 24
    print(solution(brown, yellow))