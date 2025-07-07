from sys import stdin

def main():
    while True:
        N = int(stdin.readline())
        if N == -1 :
            break

        divisor = []
        for i in range(1,N):
            if N % i == 0:
                divisor.append(i)

        if sum(divisor) == N:

            string = ' + '.join( str(d) for d in sorted(divisor))
            print(f"{N} = {string}")

        else:
            print(f"{N} is NOT perfect.")


if __name__=="__main__":
    main()