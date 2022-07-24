def digit_sum(x):
    total = 0
    while x > 0:
        total += x % 10
        x //= 10
    return total


n = int(input())
input_array = list(map(int, input().split()))
result = []
for value in input_array:
    result.append(digit_sum(value))

max_value = max(result)
for idx, x in enumerate(result):
    if x == max_value:
        print(input_array[idx])
        break


"""
3
125 15232 97
"""