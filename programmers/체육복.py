def solution(n, lost, reserve):
    answer = []
    lost = set(lost)
    reserve = set(reserve)

    same = lost.intersection(reserve)

    lost -= same
    reserve -= same

    lost = list(lost)
    reserve = list(reserve)

    for x in lost:
        for y in reserve:
            if abs(x-y) == 1:
                answer.append(x)
                reserve[reserve.index(y)] = 9999
                break 
    

    if answer == lost:
        return n
    
    elif len(answer) < len(lost) : 
        return n - len(lost) + len(answer)



if __name__ == '__main__': 
    n = 3
    lost = [3]
    # reserve = [1,3,5]
    reserve = [1]
    print(solution(n,lost,reserve)) 