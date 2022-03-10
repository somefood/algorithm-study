M = int(input())
N = int(input())

result = []
for i in range(M, N+1):

    # if i % 2 == 0:
    #     continue

    is_prime = False
    for j in range(2, i):
        if i % j == 0:
            is_prime = True
            break

    if not is_prime:
        result.append(i)

print(result)
if len(result) <= 0:
    print(-1)
else:
    print(sum(result))
    print(result[0])

"""
60
100

620
61
"""