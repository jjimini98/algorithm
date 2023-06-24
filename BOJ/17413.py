from sys import stdin

input = stdin.readline


S = input().rstrip()


answer = []
flag = 0 #0이면 <> 포함 x , 1이면 <> 포함
tmp = ''


def reverse(tmp : str) :
    return tmp[::-1]


for s in S:

    if s == "<":
        if len(tmp) != 0 and flag == 0:
            answer.append(reverse(tmp))
            answer.append("<")
            tmp = ''
            flag = 1
        else:
            tmp += s
            flag = 1

    elif s == ">":
        tmp += s
        flag = 0
        answer.append(tmp)
        tmp = ''

    elif s == " ":
        if flag == 1:
            tmp += s
        else:
            if len(tmp) != 0:
                answer.append(reverse(tmp))
                answer.append(' ')
                tmp = ''
    else:
        tmp += s


if len(tmp) != 0 :
    answer.append(reverse(tmp))
    tmp = ''


print(''.join(answer))
