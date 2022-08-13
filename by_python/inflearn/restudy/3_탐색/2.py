word = input()

num = ""
for w in word:
    if w.isdigit():
        num += w

num = int(num)
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1

print(num)
print(count)

"""
g0en2Ts8eSoft
"""