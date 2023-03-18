def solution(sizes):

    x = []
    y = [] 
    for s in sizes:
        x.append(max(s))
        y.append(min(s))

    return max(x)*max(y)



if __name__ == '__main__': 
    # s = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
    s = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
    print(solution(s))