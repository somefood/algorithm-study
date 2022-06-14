from collections import defaultdict

n = int(input())
card1 = list(map(int, input().split()))
card_dict = defaultdict(int)
for card in card1:
    card_dict[card] += 1

m = int(input())
card2 = list(map(int, input().split()))

for card in card2:
    print(card_dict[card], end=" ")

"""
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10
"""