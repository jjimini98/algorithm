from sys import stdin

input = stdin.readline

N = int(input())
loss = list(map(int, input().split()))
geunyuk = []


loss.sort()

if N % 2 == 1:
    geunyuk.append(loss[-1])
    loss = loss[:-1]

print(loss)

# if N == 1:
#     geunyuk = loss[0]
#
# if N != 1 and N % 2 != 0 :
#     for x in loss:
#         for y in range(N-2,-1,-1):
#             if x == loss[y]:
#                 continue
#             else:
#                 geunyuk = max(x + loss[y], geunyuk)
#         N -= 1
#
# else:
#     for x in loss:
#         for y in range(N-1,-1,-1):
#             if x == loss[y] :
#                 continue
#             else:
#
#                 geunyuk = max(x+loss[y],geunyuk)
#         N -= 1
#
# print(geunyuk)