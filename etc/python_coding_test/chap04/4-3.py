# position = 'intput()'
position = 'a1'

horizion = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
vertical = ['1', '2', '3', '4', '5', '6', '7', '8']

# 경우
# -2 -1
# -2 1
# 2 -1
# 2 1

# -1 -2
# 1 -2
# -1 2
# 1 2

dx = [-2, -2, 2, 2, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, -2, -2, 2, 2]

x = horizion.index(position[0])
y = vertical.index(position[1])

count = 0
for i in range(8):
    if x + dx[i] < 0 or x + dx[i] >=8 or y + dy[i] < 0 or y + dy[i] >=8:
        continue
    count += 1

print(count)
