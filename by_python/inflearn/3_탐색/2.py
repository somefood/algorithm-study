word = input()

s = ""
for i in word:
    if i.isnumeric():
        s += i

value = int(s)

cnt = 0
for i in range(1, value + 1):
    if value % i == 0:
        cnt += 1

print(value)
print(cnt)