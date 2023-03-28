def solution(n):
    n_count = bin(n).count("1")


    while True:
        n += 1
        bin_count = bin(n).count("1")

        if bin_count == n_count:
            return n 




if __name__ == '__main__': 
    n = 15
    print(solution(n))