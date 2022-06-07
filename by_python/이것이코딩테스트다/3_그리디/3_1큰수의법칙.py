N, M, K = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse=True)
result = 0

first = nums[0]
second = nums[1]

count = 0
idx = 0

while True:
    for i in range(K):  # 가장 큰 수를 K 번 더하기
        if M == 0:  # m 이 0 이 라면 반복문 탈출
            break
        result += first
        M -= 1  # 더할 때마다 1 씩 빼기
    if M == 0:  # m 이 0 이라면 반복문 탈출
        break
    result += second  # 두 번째로 큰 수를 한 번 더하기
    M -= 1  # 더할 때마다 1 씩 빼기

print(result)

"""
5 8 3
2 4 5 4 6

5 7 2
3 4 3 4 3
"""
