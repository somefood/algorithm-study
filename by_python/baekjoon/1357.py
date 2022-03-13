a, b = input().split()

a = ''.join(list(reversed(a)))
b = ''.join(list(reversed(b)))

result = int(a) + int(b)
print(result)
result = str(result)
result = ''.join(list(reversed(result)))
print(int(result))