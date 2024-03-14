from sys import stdin

input = stdin.readline


L , R = input().rstrip().split()
word = input().rstrip()
answer = 0

# keyboard = ['zaq','xsw','cde','vfr','bgt','nhy','mju','ki','lo','p']

leftK = ['zaq','xsw','cde','vfr',' gt']
rightK = ['','','','','b  ','nhy','mju',' ki',' lo','  p']


def find_location(word : str):
    l = 'zaqxswcdevfrgt'


    if word in l :
        for i in range(5):

            if word in leftK[i]:
                for x in range(len(leftK[i])):
                    if leftK[i][x] == word:
                        return [i,x]
            else:
                continue


    else:
        for i in range(10):
            if word in rightK[i] :
                for x in range(len(rightK[i])):
                    if rightK[i][x] == word:
                        coo = [i,x]
                        return coo



lL = find_location(L)
lR = find_location(R)



for w in word:

    if w == L or w == R:
        answer += 1

    else:
        r = 'bnhymjukilop'
        coo = find_location(w)

        if w in r :
            right = abs(lR[0] - coo[0]) + abs(lR[1] - coo[1])
            answer += right
            lR = coo

        else:
            left = abs(lL[0] - coo[0]) + abs(lL[1] - coo[1])
            answer += left
            lL = coo

        answer += 1

print(answer)

        #
        #
        # left = abs(lL[0] - coo[0]) + abs(lL[1] - coo[1])
        # right =abs(lR[0] - coo[0]) + abs(lR[1] - coo[1])

        # if left <= right:
        #     answer += left
        #     lL = coo
        # else:
        #     answer += right
        #     lR = coo

        # answer += 1


# print(answer)
