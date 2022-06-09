from itertools import permutations, combinations

l = [1, 2, 3, 4]
per = permutations(l, 3)
com = combinations(l, 3)

for p in per:
    print(p)

print("============")

for c in com:
    print(c)
