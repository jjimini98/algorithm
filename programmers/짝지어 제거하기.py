# 문제풀이 방법
# stack 을 이용한 문제풀이


def solution(sen):

    stack = [sen[0]]

    for i in sen[1:]:
        if len(stack) == 0:
            stack.append(i)

        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)

    if len(stack) == 0:
        return 1
    else:
        return 0



if __name__ == "__main__":
    # s = "baaaccooba"
    s = "abccaabaa"
    print(solution(s))
