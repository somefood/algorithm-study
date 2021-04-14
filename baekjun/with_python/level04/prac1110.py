origin_num = input()
temp_num = ""
cycle = 0

if len(origin_num) <= 1:
    origin_num = "0" + origin_num
result = origin_num

while result != temp_num:
    origin_num = origin_num[1] + f"{int(origin_num[0]) + int(origin_num[1]):02d}"[1]
    temp_num = origin_num
    cycle += 1

print(cycle)