# def main(lis : list , target : int) -> list : 
#     for i in lis:
#         for j in lis:
#             if i == j :
#                 continue # 중복은 안되니깐
#             if i + j == target:
#                 print([lis.index(i),lis.index(j)])
#                 break 
#         break

def main(lis : list, target : int) -> list:
    for i in lis:
        for j in lis[1:]: #중복은 안되니까 [1:] 써도 될듯! 
            if i + j == target:
                return [lis.index(i), lis.index(j)]

#해시테이블 구현 필요


if __name__ == "__main__":
    lis = [2,7,10,19]
    target = 9
    print(main(lis,target))