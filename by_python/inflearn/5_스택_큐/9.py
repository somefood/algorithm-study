from collections import defaultdict

word1 = input()
word2 = input()

k1 = defaultdict(int)
k2 = defaultdict(int)

for x1, x2 in zip(word1, word2):
    k1[x1] += 1
    k2[x2] += 1

for k in k1.keys():
    if k in k2:
        if k1[k] != k2[k]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")

"""
AbaAeCe
baeeACA
"""