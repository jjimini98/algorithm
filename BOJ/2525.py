from sys import stdin

input = stdin.readline

hour,minutes = map(int,input().split())
ex_min = int(input())
answer = ''


need_total = ex_min + minutes

need_hour = need_total // 60 
need_min = need_total % 60

total_hour = need_hour + hour 
if total_hour < 24: 
    answer += str(total_hour)
elif total_hour == 24:
    answer += "0"
elif total_hour > 24:
    answer += str(total_hour - 24)

answer += ' '
answer += str(need_min)


print(answer)