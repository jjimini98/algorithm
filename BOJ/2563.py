from sys import stdin

input = stdin.readline


def find_index(row, col): # (3,7) 입력했을 때 (3,7)~(13,17)까진 나왔으면 하는거임. 인덱스 별로
    result = []
    x = [ x for x in range(row, row+11)]
    y = [ y for y in range(col, col+11)]

    for i in x :
        for j in y:
            result.append([i, j])
    # print(result)
    return result

def main(idx_list : list):
    white = [[0 for _ in range(10)] for _ in range(10)]
    total = 100 * len(idx_list)
    # find_index(idx_x, idx_y)
    final = []
    for idx in idx_list: # (3,7) , (5,2)
        idx_x, idx_y = idx[0], idx[1]
        for item in find_index(idx_x, idx_y):
           if item not in final :
               continue
           # else:


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

if __name__ == "__main__":
    idx_list = []
    for _ in range(int(input())):
        lis = list(map(int, input().split()))
        idx_list.append(lis)
    main(idx_list)
# print("==========================================")
# print(find_index(5,2))


#
# for x in find_index(row, col):
#     for i in range(10):
#         for j in range(10):
#             if x[0] == i and x[1] == j:
#                 white[i][j] += 1

