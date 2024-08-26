import sys
input = sys.stdin.readline

def is_prime_number(N):
    for i in range(2, N):
        if N % i == 0:
            return False  # 소수가 아님
    return True  # 소수임

# def



def main():
    N = int(input())
    number = 2
    while True  :
        isprime = is_prime_number(number)
        if isprime == True: # 소수면 최대한 나눠보고 넘어간다.
            while True:
                if N % number != 0 :
                    number += 1
                    break
                else:
                    N = N // number
                    print(number)

        if N == 1:
            break


if __name__ == '__main__':
    main()