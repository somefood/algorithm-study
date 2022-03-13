s = input()

length = len(s)

a = length // 10
b = length % 10

for i in range(a):
    start = i * 10
    end = i * 10 + 10
    print(s[start:end])

print(s[a*10:a*10+b])
