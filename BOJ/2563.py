from sys import stdin
input = stdin.readline


N = int(input())
array = [[0] * 100 for _ in range(100)]  # 도화지 범위 초기화
for _ in range(N):  # 입력 받은 도화지 개수만큼 돈다.
    y1, x1 = map(int, input().split())  # 왼쪽아래 x,y 좌표를 받는다.

    for i in range(x1, x1 + 10):  # 세로를 돈다.
        for j in range(y1, y1 + 10):  # 가로를 돈다.
            array[i][j] = 1  # 해당 범위 값을 0에서 1로 바꿔준다.

result = 0  # 넓이를 출력할 변수
for k in range(100):  # 전체 도화지를 돌면서
    result += array[k].count(1)  # 1 개수만 세어준다

print(result)




# def find_index(row, col): # (3,7) 입력했을 때 (3,7)~(13,17)까진 나왔으면 하는거임. 인덱스 별로
#     result = []
#     x = [ x for x in range(row, row+11)]
#     y = [ y for y in range(col, col+11)]
#
#     for i in x :
#         for j in y:
#             result.append((i, j))
#     # print(result)
#     return result
#
# for _ in range(int(input())):
#     final_lis = []
#     idx = list(map(int, input().split()))
#     lis = find_index(idx[0], idx[1])
#     final_lis.extend(lis)
#
#
# print(final_lis)


    # print(len(find_index(idx[0], idx[1])))
# def main(idx_list : list):
#     white = [[0 for _ in range(100)] for _ in range(100)]
#     total = 100 * len(idx_list)
#     # find_index(idx_x, idx_y)
#     final = []
#     for idx in idx_list: # (3,7) , (5,2)
#         idx_x, idx_y = idx[0], idx[1]
#         for item in find_index(idx_x, idx_y):
#            if item not in final :
#                continue
#            # else:


    #     for row in range(10):
    #         for col in range(10):
    #             for spec in find_index(idx_x, idx_y):
    #                 if [row, col] == spec:
    #                     white[row][col] += 1

    # print(white)



        # for row in range(10):
        #     for col in range(10):
        #         for spec in find_index(idx_x, idx_y):
        #             if row == spec[0] and col == spec[1]:
        #                 white[row][col] += 1

    # print(white)

# if __name__ == "__main__":
#     idx_list = []
#     for _ in range(int(input())):
#         lis = list(map(int, input().split()))
#         idx_list.append(lis)
#     main(idx_list)
# print("==========================================")
# print(find_index(5,2))


#
# for x in find_index(row, col):
#     for i in range(10):
#         for j in range(10):
#             if x[0] == i and x[1] == j:
#                 white[i][j] += 1

