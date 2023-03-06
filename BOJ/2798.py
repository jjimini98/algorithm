from sys import stdin
from itertools import combinations

input = stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))
sum_cards = 0 

for combi in combinations(cards,3):
    sum_combi = sum(combi)
    if sum_combi <= M :
        sum_cards = max(sum_cards, sum_combi)

print(sum_cards)

