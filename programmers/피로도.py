from itertools import permutations

def solution(k, dungeons):
    answer = 0 
    for combi in permutations(dungeons, len(dungeons)):
        tmp = 0 
        heart = k 
        for need, min in combi:
            if heart >= need:
                heart -= min
                tmp += 1
            answer = max(answer,tmp)
    return answer





if __name__ == '__main__': 
    k = 80
    dungeons = [[80,20],[50,40],[30,10]]
    print(solution(k,dungeons))