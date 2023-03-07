def solution(arr):
    answer = [arr[0]]

    for x in arr[1:]:
        if answer[-1] == x:
            continue
        else:
            answer.append(x)
    return answer 



if __name__ == '__main__': 
    arr = [1,1,3,3,0,1,1]
    print(solution(arr))