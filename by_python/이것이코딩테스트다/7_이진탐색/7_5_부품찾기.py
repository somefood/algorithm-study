import sys


def search(need):
    start = 0
    end = len(stock)

    while start <= end:
        mid = (start + end) // 2

        if stock[mid] == need:
            return True

        if stock[mid] > need:
            end = mid - 1
        else:
            start = mid + 1
    return False


input = sys.stdin.readline

n = int(input().rstrip())
stock = list(map(int, input().split()))
stock.sort()

m = int(input().rstrip())
needs = list(map(int, input().split()))

for need in needs:
    if search(need):
        print("yes", end=" ")
    else:
        print("no", end=" ")

"""
5
8 3 7 9 2
3
5 7 9
"""