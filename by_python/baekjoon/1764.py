from collections import defaultdict

people = defaultdict(int)

n, m = map(int, input().split())

for _ in range(n):
    people[input()] += 1

for _ in range(m):
    people[input()] += 1

result = []

for k, v in people.items():
    if v == 2:
        result.append(k)

result.sort()

print(len(result))
for p in result:
    print(p)


"""
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton
"""