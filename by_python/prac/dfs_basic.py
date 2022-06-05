def dfs(depth):

    if depth == K:
        print(result)
        return

    for i in range(N):
        if arr[i] in result:
            continue
        result.append(arr[i])
        dfs(depth + 1)
        result.pop()


if __name__ == "__main__":
    N, K = map(int, input().split()) # 4 2
    arr = [i for i in range(1, N + 1)]
    result = list()
    dfs(0)


