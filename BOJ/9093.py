from sys import stdin

input = stdin.readline


for _ in range(int(input())):
    sentence = input().rstrip().split(" ")
    reve = [] 

    for word in sentence:

        if len(word) >= 2:
            word = list(word)[::-1]
            reve.append(''.join(word))

        else: 
            reve.append(word)
    
    print(' '.join(reve))