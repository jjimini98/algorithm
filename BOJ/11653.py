import sys
input = sys.stdin.readline

def is_prime_number(N):
    for i in range(2, N):
        if N % i == 0:
            return False  # 소수가 아님
    return True  # 소수임

def main():
    N = int(input())
    while N == 0: