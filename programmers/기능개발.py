# 정답코드
def solution(progresses, speeds):

    answer = []
    time = 0
    count = 0
    
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100: 
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer


# from math import ceil
# def solution(progresses, speeds):
#     answer = []
#     count = 1
#     days = [ceil((100-p)/s) for p,s in zip(progresses, speeds)]

#     stack = [days[0]]
#     for day in days[1:]:
#         if stack[-1] < day:
#             answer.append(count)
#             count = 1
#         else:
#             count += 1
#     answer.append(count)
#     return answer


if __name__ == '__main__':
    # progress = [95,90,99,99,80,99]
    # speed = [1,1,1,1,1,1]
    # progress = [93, 30, 55]
    # speed = [1,30,5]
    progress = [99,99,99,90,90,90]
    speed = [1,1,1,1,1,1]
    print(solution(progress,speed))
