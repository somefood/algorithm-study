counter = 0 # 나눗셈 횟수 카운트
ptr = 0 # 이미 찾은 소수의 개수
prime = [None] * 500

prime[ptr] = 2
ptr += 1

for n in range(3, 1001, 2):
    for i in range(1,ptr):
        counter += 1
        if n % prime[i] == 0:
            break
    else:
        print('ptr:', ptr)
        prime[ptr] = n
        ptr += 1

for i in range(ptr):
    print(prime[i])
print(counter)