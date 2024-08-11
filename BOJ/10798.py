from sys import stdin

input = stdin.readline

words = []
for _ in range(5):
    lis =list(input().split("\n")[0])
    words.append(lis)
# print(words)

new_word = []
max_len = 0
for word in words:
    max_len = max(max_len, len(word))
    if len(word) < max_len:
        v = max_len - len(word)
        for _ in range(v):
            word += ' '
            new_word.append(word)
    else:
        new_word.append(word)
for d in range(len(word)):
    for word in new_word:


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