import sys

input = sys.stdin.readline

n = int(input())
time = []
for _ in range(n):
    start, end = map(int, input().split())
    time.append((start, end))

# 1. 끝나는 시간의 오름차순
# 2. 시작하는 시간의 오름차순
time.sort(key=lambda x: (x[1], x[0]))
cnt = 1
end_time = time[0][1]
for i in range(1, n):
    if time[i][0] >= end_time:
        cnt += 1
        end_time = time[i][1]

print(cnt)


"""
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
"""