import collections

t = int(input())

for _ in range(t):
    result = [0 for i in range(26)]
    word = input()

    for w in word:
        result[ord(w) - 65] += 1

    hap = 0
    for num, i in enumerate(result, start=65):
        if i == 0:
            hap += num
    print(hap)




