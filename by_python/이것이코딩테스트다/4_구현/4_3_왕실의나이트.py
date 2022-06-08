rows = ["1", "2", "3", "4", "5", "6", "7", "8"]
cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

position = input()
col = position[0]
row = position[1]

dx = [-2, -2, -1, 1, 2, 2, -1, 1]
dy = [-1, 1, 2, 2, -1, 1, -2, -2]

row = rows.index(row)
col = cols.index(col)

count = 0

for i in range(len(dx)):

    nx = row + dx[i]
    ny = col + dy[i]

    if nx < 0 or ny < 0 or nx >= 8 or ny >= 8:
        continue
    count += 1

print(count)