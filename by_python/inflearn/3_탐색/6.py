n = int(input())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

row = []
col = []
diagonal = []

for i in grid:
    row.append(sum(i))

for i in range(len(grid)):
    value = 0
    for j in range(len(grid)):
        value += grid[j][i]
    col.append(value)

value = 0
for i in range(n):
    value += grid[i][i]
diagonal.append(value)

value = 0
for i in range(n):
    value += grid[i][n-i-1]
diagonal.append(value)

print(row)
print(col)
print(diagonal)

print(max(max(row), max(col), max(diagonal)))

