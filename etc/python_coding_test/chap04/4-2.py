n = int(input())

hour_to_second = n * 60 * 60
minute_to_second = 59 * 60
second = 59

total_hour = hour_to_second + minute_to_second + second

count = 0
for i in range(total_hour):
    hour = i // 3600
    minute = i % 3600 // 60
    second = i % 3600 % 60
    if "3" in f"{hour}{minute}{second}":
      count += 1

print(count)