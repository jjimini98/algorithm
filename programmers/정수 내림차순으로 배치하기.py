def solution(n):
    SN = str(n)
    sort_SN = sorted(SN,reverse=True)
    return int(''.join(sort_SN))


if __name__ == "__main__":
    n = 118372
    print(solution(n))