def recur(n: int) -> int:
    while  n > 0:
        recur(n - 1)
        print(n)
        n = n - 2