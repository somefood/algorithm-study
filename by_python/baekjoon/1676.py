def get_fact(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * get_fact(n-1)


def find_not_zero(string):
    string = string[::-1]
    count = 0
    for s in string:
        if s == "0":
            count += 1
            continue
        return count


def easy_way(N):
    mul5 = N // 5
    mul25 = N // 25
    mul125 = N // 125

    return mul5 + mul25 + mul125


n = int(input())

print(easy_way(n))
# fact = get_fact(n)
# print(find_not_zero(str(fact)))

