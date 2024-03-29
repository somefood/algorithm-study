# N, M 을 공백으로 구분하여 입 력받기
n, m = map(int, input().split())
result = 0
# 한 줄씩 입력 받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 ’ 가장 작은 수 ’ 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    # ' 가장 작은 수 ' 둘 중에 서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)  # 최종 답안 출력

"""
3 3
3 1 2
4 1 4
2 2 2

2 4
7 3 1 8
3 3 3 4
"""
