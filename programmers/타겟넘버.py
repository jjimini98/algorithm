from collections import defaultdict

def dfs(graph, start):

    need_visited, visited = list(), list()
    # answer = 0
    ## 시작 노드를 시정하기 
    need_visited.append(start)
    
    ## 만약 아직도 방문이 필요한 노드가 있다면,
    while need_visited:
 
        ## 그 중에서 가장 마지막 데이터를 추출 (스택 구조의 활용)
        node = need_visited.pop()
        
        ## 만약 그 노드가 방문한 목록에 없다면
        if node not in visited:
 
            ## 방문한 목록에 추가하기 
            visited.append(node)
 
            ## 그 노드에 연결된 노드를 
            need_visited.extend(graph[node])
            
    return visited



from itertools import combinations

def solution(n, target):
    answer = []

    for i in n:
        answer.append(-i)

    n += answer
    # print(n)
    


    for combi in combinations(n , len(answer)):
        print(combi)


    # graph = defaultdict(list)

    # for x in range(len(n)-1):
    #     graph[n[x]].append(n[x+1])
    #     graph[n[x]].append(-n[x+1])
    #     graph[-n[x]].append(n[x+1])
    #     graph[-n[x]].append(-n[x+1])



    # # print(graph)
    # print(dfs(graph,4))





    return answer



if __name__ == '__main__': 
    numbers = [4,1,2,1]
    target = 4
    print(solution(numbers,target))