from collections import defaultdict

def solution(clothes):

    answer = 1
    kind = dict() 
    for cloth in clothes:
        if cloth[1] in kind: 
            kind[cloth[1]] += 1 
        else: 
            kind[cloth[1]] = 1

    for k,v in kind.items():
        answer *= (v + 1)
    
    
    return answer -1 



if __name__ == '__main__': 
    clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    print(solution(clothes))