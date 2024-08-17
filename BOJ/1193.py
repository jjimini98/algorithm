import time
from sys import stdin

start = time.time()  # 시작 시간 저장

def main(N):

    num = 0

    if N == 1 : return "1/1"

    for idx in range(1,N+1):
        for i, j in zip(range(1, idx + 1), range(idx, 0, -1)):
            num += 1
            if num == N :
                if N % 2  == 0 :
                    return  f"{i}/{j}"
                else:
                    return f"{j}/{i}"



if __name__ == "__main__":
    N = int(stdin.readline())
    print(main(N))

