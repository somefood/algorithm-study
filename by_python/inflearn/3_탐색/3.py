# card = [i for i in range(1, 21)]
card = [i for i in range(21)]

for _ in range(10):
    a, b = map(int, input().split())

    # print(card[:a-1])
    # print(list(reversed(card[a - 1:b])))
    # print(card[b:])
    # card = card[:a-1] + list(reversed(card[a-1:b])) + card[b:]
    """강의 답"""
    for i in range((b-a+1)//2):
        card[a+i], card[b-i] = card[b-i], card[a+i]

card.pop(0)
print(card)
