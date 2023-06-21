from sys import stdin

input = stdin.readline

def solution(board : str):

    for bo in board.split("."):
        if len(bo) % 2 != 0 :
            return -1

    tmp = []
    answer = ''

    for i in board+" ":
        if i == "X":
            tmp.append("X")
        else:
            if tmp.count("X") == 2:
                answer += "BB"
            else:
                share = tmp.count("X") // 4
                ing = tmp.count("X") % 4

                answer += "AAAA" * share
                if ing != 0:
                    answer += "BB"

            answer += "."
            tmp = []

    return answer[:-1]

if __name__ == '__main__':
    board = input().rstrip()
    print(solution(board))
