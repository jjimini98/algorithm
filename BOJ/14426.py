# 시간초과아아악!!!!!!!!!!!!!
# from sys import stdin

# input = stdin.readline

# N, M = map(int, input().split())
# word_list = [input().rstrip() for _ in range(N)]
# std_list = [input().rstrip() for _ in range(M)]

# answer = 0 

# def cutting(standard : str):
#     for word in word_list:
#         if word[0] == standard[0] and standard == word[:len(standard)]:
#             return 1




# for std in std_list:

#     if cutting(std) == 1:
#         answer += 1


# print(answer)




from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
word_list = [input().strip() for _ in range(N)]

answer = 0 


for _ in range(M):
    standard = input().rstrip()

    for i in range(N):
        if word_list[i].startswith(standard):
            answer+=1 
            break


print(answer)