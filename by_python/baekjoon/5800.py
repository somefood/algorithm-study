import sys

k = int(input())

for i, _ in enumerate(range(k), start=1):
    split = input().split()
    result = list(map(int, split[1:]))
    result.sort(reverse=True)
    max_value = max(result)
    min_value = min(result)

    v = -sys.maxsize
    for j in range(len(result) - 1):
        v = max(v, result[j] - result[j + 1])
    print(f"Class {i}")
    print(f"Max {max_value}, Min {min_value}, Largest gap {v}")
