n = int(input())

for i in range(n):
    s = input().lower()

    v = ""
    if s == s[::-1]:
        v = "YES"
    else:
        v = "NO"
    print(f"#{i + 1} {v}")
