def solution(sizes):
    widthes = [a*b for a,b in sizes]
    x = sizes[widthes.index(max(widthes))][0]
    y = sizes[widthes.index(max(widthes))][1]

    print(widthes)
    print(x)
    print(y)
    for a,b in sizes:
        x = max(x,a)
        y = max(y,b)
    print(x)
    print(y)
    return x*y



if __name__ == '__main__': 
    # s = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
    s = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
    print(solution(s))