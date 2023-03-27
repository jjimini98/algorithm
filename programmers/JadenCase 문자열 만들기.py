from string import ascii_lowercase, ascii_uppercase

def solution(s):
    answer = ''
    
    s = s.lower().split(' ')
    
    for word in s:
        if word == '':
            answer += ' '
            continue

        if word[0] in ascii_lowercase:
            idx = ascii_lowercase.index(word[0])
            answer += ascii_uppercase[idx]
            answer += word[1:]
        else:
            answer += word
        answer += ' '

    return answer[:-1]




if __name__ == '__main__': 
    s = "3people unFollowed me"
    s2  = "for   the last week"

    print(solution(s))
    print(solution(s2))