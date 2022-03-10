import math

M = int(input())
N = int(input())

i = 1
result = []
while True:
    multi = i * i
    if M <= multi <= N:
        result.append(multi)
    if multi > N:
        break
    i += 1

if len(result) <= 0:
    print(-1)
else:
    print(sum(result))
    print(result[0])

