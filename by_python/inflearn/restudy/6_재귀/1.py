def dfs(n):
    global result
    if n == 1:
        result = "1" + result
        return

    dfs(n // 2)
    result += str(n % 2)


def dfs_lecture(x):
    if x == 0:
        return

    else:
        dfs_lecture(x//2)
        print(x % 2, end="")


result = ""
n = int(input())
dfs(n)
print(result)