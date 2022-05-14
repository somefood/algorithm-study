def check_visit(idx):
    for i in range(4):
        x = idx[0] + dx[i]
        y = idx[1] + dy[i]

        if x < 0 or x >= R or y < 0 or y >= C:
            continue
        alpha_idx = ord(arr[x][y]) - 65
        if alpha[alpha_idx] == 0:
            return False
    return True


def dfs(idx, depth):
    global max_value
    if check_visit(idx):
        max_value = max(max_value, depth)
        return

    cur_x = idx[0]
    cur_y = idx[1]

    for i in range(4):
        x = cur_x + dx[i]
        y = cur_y + dy[i]

        if x < 0 or x >= R or y < 0 or y >= C:
            continue
        alpha_idx = ord(arr[x][y]) - 65
        if visited[x][y] == 1 or arr[x][y] == arr[cur_x][cur_y] or alpha[alpha_idx] >= 1:
            continue

        alpha[alpha_idx] += 1
        visited[x][y] = 1
        dfs((x, y), depth + 1)
        alpha[alpha_idx] -= 1
        visited[x][y] = 0


max_value = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
alpha = [0] * 26


alpha[ord(arr[0][0])-65] = 1
visited[0][0] = 1
dfs((0, 0), 1)
print(max_value)
"""
2 4
CAAB
ADCB
"""