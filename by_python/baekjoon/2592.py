arr = [int(input()) for i in range(10)]

print(int(sum(arr)/10))

s = list(set(arr))

max_count = [arr.count(num) for num in s]
print(s[max_count.index(max(max_count))])