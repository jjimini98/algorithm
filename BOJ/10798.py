from sys import stdin

input = stdin.readline

def refine_maxlen(lis : list, max_len):
    nec = max_len-len(lis)
    for i in range(nec):
        lis.append(' ')
    return lis

words = []

for _ in range(5):
    words.append(list(input().split("\n")[0]))

refine_words = []
max_len = 0
for word in words: #여기서 뭔가 잘못된듯하다. def를 타지 않음
    if len(word) >= max_len:
        max_len = len(word)
        refine_words.append(word)
    else:
        refine_words.append(refine_maxlen(word,max_len))

final_word = []
for i in range(max_len):
    lis = []
    for word in refine_words:
        print(word)
        try:
            lis.append(word[i])
        except:
            continue
    final_word.append(lis)

result = ''
for i in range(len(final_word)):
    row = ''.join(final_word[i])
    row = row.replace(" ", '')
    result += row
print(result)

