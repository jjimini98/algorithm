from sys import stdin

input = stdin.readline

# words = []
# for _ in range(5):
#     lis =list(input().split("\n")[0])
#     words.append(lis)
# # print(words)
#
# new_word = []
# max_len = 0
# for word in words:
#     max_len = max(max_len, len(word))
#     if len(word) < max_len:
#         v = max_len - len(word)
#         for _ in range(v):
#             word += ' '
#             new_word.append(word)
#     else:
#         new_word.append(word)
# for d in range(len(word)):
#     for word in new_word:


# i = 0
# for _ in
#     for word in new_word:
#         for i in range(len(word)):#
#             result += word[i]
#             break
#     i += 1
#
# result = result.replace(' ', '')
# print(result)


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
for word in words:
    if len(word) >= max_len:
        max_len = len(word)
        refine_words.append(word)
    else:
        refine_words.append(refine_maxlen(word,max_len))

final_word = []
for i in range(max_len):
    lis = []
    for word in refine_words:

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

