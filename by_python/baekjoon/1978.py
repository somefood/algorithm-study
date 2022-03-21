def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


n = int(input())

lst = map(int, input().split())

cnt = 0
for l in lst:
    if is_prime(l):
        cnt += 1

print(cnt)
