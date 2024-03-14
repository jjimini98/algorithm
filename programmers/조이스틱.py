def solution(name):

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sindex = 0
    eindex = 25
    answer = 0

    def remove_A(name:str):
        new_name = ''
        count = 0 
        for n in name:
            if n == "A":
                count += 1
            
            else: 
                new_name += n
                if count >=2 :
                    new_name += "A"
                    count = 0 



    if name == "A" * len(name) : 
        return 0

    if name[1:-1] == "A"* (len(name)-2) : 
        name = name[0] + name[-1]
        # print(name)

    elif name[1] == "A":
        name = name[0] + name[1:][::-1]
        name = name[:-1]
        # print(name)
    elif name[-1] == "A"
    for x in name:
        idx = alpha.index(x)

        if abs(sindex - idx) <= abs(eindex - idx):
            answer += abs(sindex-idx)
        
        else:
            answer += abs(eindex-idx) + 1

        answer +=1 


    return answer -1 





if __name__ == '__main__': 
    name = "LAABAA"
    
    print(solution(name))