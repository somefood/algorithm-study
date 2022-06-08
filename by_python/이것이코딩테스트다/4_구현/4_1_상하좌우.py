# n = int(input())
# x, y = 1, 1
# plans = input().split()
# # L, R, U, D 에 따른 이동 방향
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_types = ['L', 'R', 'U', 'D']
# # 이동 계획을 하나씩 확인
# for plan in plans:
#     # 이동 후 좌표 구하기
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     # 공간을 벗어나는 경우 무시
#     if nx < 1 or ny < 1 or nx > n or ny > n :
#         continue
#     # 이동 수행
#     x, y = nx, ny
# print(x, y)


from collections import deque

n = int(input())
arr = [[0] * n for _ in range(n)]
direct = {
    "R": [0, 1],
    "L": [0, -1],
    "U": [-1, 0],
    "D": [1, 0],
}
Q = deque(input().split())
x = 0
y = 0
while Q:
    pop_x, pop_y = direct[Q.popleft()]

    if x + pop_x < 0 or x + pop_x >= n or y + pop_y < 0 or y + pop_y >= n:
        continue
    x += pop_x
    y += pop_y

print(x + 1, y + 1)



"""
5
R R R U D D
"""