import sys
n, m, b = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
height = 0
ans = sys.maxsize

for target in range(257):
    max_value = 0
    min_value = 0
    for i in range(n):
        for j in range(m):
            if table[i][j] < target:
                min_value += (target - table[i][j])
            else:
                max_value += (table[i][j] - target)
    inventory = max_value + b
    if inventory < min_value:
        continue
    time = 2 * max_value + min_value
    if time <= ans:
    # 시간이 같을 때는 높이가 높은 순으로 출력하라는 조건에 맞게
    # for i in range(257)은 항상 i가 오름차순으로 돌기 때문에
    # 시간이 같아도 최종적으로는 높이가 높은 순으로 나오게 된다
        ans = time
        height = target
print(ans, height)


"""
3 4 99
0 0 0 0
0 0 0 0
0 0 0 1
"""