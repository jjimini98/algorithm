from collections import defaultdict

def solution(genres, plays):
    answer = []
    t_answer = [] 
    total = defaultdict(list)
    count = defaultdict(int)

    for g , p in zip(genres, plays):
        
        total[g].append(p)
        count[g] += p 

    s_count = sorted(count.items(), key = lambda x : -x[1])

    for genre, _ in s_count:
        listen = sorted(total.get(genre),reverse= True)
        if len(listen) != 1:
            t_answer.extend(listen[:2])
        else:
            t_answer.extend(listen)
    
    # 조건을 꼼꼼히 읽어보자..
    for x in t_answer:
        idx = plays.index(x)
        answer.append(idx)
        plays[idx] = ''

    return answer 




if __name__ == '__main__': 
    # genres = ["classic", "pop", "classic", "classic", "pop"]
    # plays = [500, 600, 500, 800, 2500]
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [800, 600, 150, 800, 2500]
    print(solution(genres, plays))