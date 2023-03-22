from collections import deque

def solution(priorities, location):
    answer = []
    priorities = deque(priorities)
    pr = deque([])
    for idx, p in enumerate(priorities):
        pr.append((idx,p))

    for max_v in sorted(priorities , reverse=True):
        while pr:
            first = pr.popleft()

            if first[1] == max_v:
                answer.append(first)
                break
            else:
                pr.append(first)

    for x in range(len(answer)):
        if answer[x][0] == location:
            return x+1



if __name__ == '__main__': 
    # print(solution([2,1,3,2],2))
    print(solution([1, 1, 9, 1, 1, 1],0))