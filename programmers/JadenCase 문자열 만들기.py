def solution(s):
    answer = ''

    s = s.lower().split(' ')
    
    for word in s:
        if word == '':
            answer += ' '
            continue
        answer += word.capitalize()
        answer += ' '
        
    return answer[:-1]




if __name__ == '__main__': 
    s = "3people unFollowed me"
    s2  = "for   the last week"

    print(solution(s))
    print(solution(s2))