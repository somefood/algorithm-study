n = int(input())

player = []
for i in range(n):
    weight, height = map(int, input().split())
    player.append((weight, height))

player.sort(reverse=True)
cnt = 0
largest = 0

for x, y in player:
    if y > largest:
        largest = y
        cnt += 1

# 비효율적 풀이
# for i in range(len(player)):
#     for j in range(len(player)):
#         if i == j: continue
#         if player[i][0] < player[j][0] and player[i][1] < player[j][1]:
#             break
#     else:
#         cnt += 1

print(cnt)

"""
5
172 67
183 65
180 70
170 72
181 60
"""