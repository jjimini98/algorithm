
from sys import stdin

def plus_value(N):
    if N == 1: return "1/1"
    else:
        num = 1
        for i in range(2,N+1):
            num += i
            if num >= N:
                return i,num



def main(N): # N은 input 으로 입력되는 숫자
    if N == 1 : return "1/1"
    i,num = plus_value(N)
    arr = [x for x in range(1,i+1)]
    reverse_arr = list(reversed(arr))
    answers = []
    if i %2 == 0:
        for a,r in zip(arr,reverse_arr):
            answers.append("{}/{}".format(r,a))
        answers = answers[abs(num-N)]

    else :
        for a,r in zip(arr,reverse_arr):
            answers.append("{}/{}".format(a,r))
        answers = answers[abs(num-N)]
    return answers

if __name__ == "__main__":
    N = int(stdin.readline())
    print(main(N))