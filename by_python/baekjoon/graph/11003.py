# TODO: 다시 풀기, deque 활용법을 익히자

from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split(' '))

arr = list(map(int, input().split(' ')))
q = deque()
ans = []
for i in range(n):
    # 맨 뒤의 요소의 값이 크면 빼버리기, 어차피 우리가 필요한건 작은 값이니까
    while q and q[-1][0] > arr[i]:
        q.pop()
    # 인덱스를 벗어나면 보내주기, 잘 써먹었다~
    while q and q[0][1] < i - k + 1:
        q.popleft()
    q.append((arr[i], i))
    # 맨 앞에꺼 계속 써먹으면 됨
    print(q[0][0], end=' ')

"""
12 3
1 5 2 3 6 2 3 7 3 5 2 6
"""
