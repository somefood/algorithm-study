n = int(input())
direct = input().split()
arr = [[None] * n] * n

row = 0
col = 0

for i in direct:
  if i == 'L':
    if col - 1 < 0:
      continue
    col -= 1
  elif i == 'R':
    if col + 1 >= len(arr):
      continue
    col += 1
  elif i == 'U':
    if row - 1 < 0:
      continue
    row += 1
  else:
    if row + 1 >= len(arr):
      continue
    row += 1

print(row + 1, col + 1)