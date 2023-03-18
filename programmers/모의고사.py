def make_answer(length):
    total = [] 
    pattern = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]

    for stu in pattern:
        if length <= len(stu):
            total.append(stu[:length])
        else:
            share = length // len(stu)
            remain = length % len(stu)
            total.append( (stu*share) + stu[:remain] ) 
    
    return total 


def solution(answers):
    answer = []
    
    answer_list = make_answer(len(answers))
    rank = {} 
    high = 0 
    for an in answer_list:
        cor = 0 
        for correct, x in zip(answers,an):
            if correct == x:
                cor += 1 
        high = max(cor,high)
        rank[answer_list.index(an)+1] = cor


    for k,v in rank.items():
        if v == high : 
            answer.append(k)
    

    return sorted(answer)



if __name__ == '__main__': 

    answer = [1,2,3,4,5,1,2,3,4,5] 
    print(solution(answer))