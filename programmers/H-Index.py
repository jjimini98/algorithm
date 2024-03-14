# def solution(citations):
#     cite = 1
#     answer = [] 
#     n = len(citations)
#     paper = [] 
#     for _ in range(max(citations)):
#         paper = [x for x in citations if x >= cite]
#         if len(paper) >= cite and (n - len(paper)) <= cite:
#             answer.append(cite)
#         cite += 1 
#     if len(answer) == 0 : return 0
#     else: return answer[-1]



def solution(citations):
    citations.sort(reverse=True)
    # answer = max(map(min, enumerate(citations, start=1)))
    print(list(map(min, enumerate(citations, start=1))))
    # return answer

if __name__ == '__main__': 
    citation = [3,0,6,1,5]
    # citation = [0,0,0]
    print(solution(citation))   