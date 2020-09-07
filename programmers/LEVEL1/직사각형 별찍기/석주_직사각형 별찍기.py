n, m = map(int, input().strip().split(' '))

for i in range(m):
    print('*' * n)


"""
이중 배열로 하면 비효율 적이 될 수 있으니 다시 한번 생각해보자.
n, m = map(int, input().strip().split(' '))

for i in range(m):
    for j in range(n):
        print('*', end='')
    print()
"""