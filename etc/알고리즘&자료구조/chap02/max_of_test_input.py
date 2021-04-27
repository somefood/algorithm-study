from max import max_of


number = 0
x = []

while True:
    s = input()
    if s == 'End':
        break
    x.append(int(s))
    number += 1

print(number)
print(max_of(x))