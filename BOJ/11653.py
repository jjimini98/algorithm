# import sys
# input = sys.stdin.readline
#
# def is_prime_number(N):
#     for i in range(2, N):
#         if N % i == 0:
#             return False  # 소수가 아님
#     return True  # 소수임
#
# # def
#
#
#
# def main():
#     N = int(input())
#     number = 2
#     while True  :
#         isprime = is_prime_number(number)
#         if isprime == True: # 소수면 최대한 나눠보고 넘어간다.
#             while True:
#                 if N % number != 0 :
#                     number += 1
#                     break
#                 else:
#                     N = N // number
#                     print(number)
#
#         if N == 1:
#             break
#
#
# if __name__ == '__main__':
#     main()
from sys import stdin
import math



# 정해진 N 이라는 숫자 전까지 있는 모든 소수 구하기

def get_prime_number(N):
    prime = []

    array = [True for _ in range(N+1)]

    for i in range(2, int(math.sqrt(N))+1):
        if array[i] == True:
            j = 2
            while i * j <= N:
                array[i * j] = False
                j += 1

    for i in range(2,N+1):
        if array[i]:
            prime.append(i)

    return prime


def main(N):
    answer = []
    prime = get_prime_number(N)
    for i in prime:
        while True:
            if N % i == 0:
                answer.append(i)
                N = N // i
            else :
                break

    for an in sorted(answer) :
        print(an)





if __name__  == "__main__":
    N = int(stdin.readline())
    main(N)


