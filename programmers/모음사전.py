from itertools import product

def solution(word):

    dictionary = [] 
    for x in range(1,6):
        for y in product(["A","E","I","O","U"],repeat = x):
            dictionary.append(''.join(y))

    dictionary = sorted(dictionary)

    return dictionary.index(word)+1
    
if __name__ == '__main__': 
    word = "AAAAE"
    print(solution(word))