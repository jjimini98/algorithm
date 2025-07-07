from sys import stdin


def main():
    while True:
        a,b = map(int, stdin.readline().split())
        if a == 0 & b == 0:
            break
        if a % b == 0 :
             print("multiple")
        elif b % a == 0 :
            print( "factor")
        else:
             print("neither")

if __name__ == '__main__':
   main()