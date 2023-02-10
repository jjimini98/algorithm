def list_chunk(n,lst):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

def solution(n, words):
    answer = []
    inspect = [words[0]]

    for idx, word in enumerate(words[1:]):
        if inspect[-1][-1] == word[0] and word not in inspect:
            inspect.append(word)
        else:
            turns = list_chunk(n, words)
            for i, turn in  enumerate(turns):
                if word in turn :
                    answer.append(turn.index(word)+1)
                    answer.append(i+1)
            break

    if len(answer) == 0:
        return [0,0]
    else:
        return answer[-2:]


if __name__ == "__main__":
    n = 3
    word = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
    # word = ["hello", "one", "even", "never", "now", "world", "draw"]
    # word = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
    print(solution(n,word))

