n = int(input())

seconds = (n * 3600) + (59 * 60) + 59

count = 0
for s in range(seconds + 1):
    hour = str(s // 3600)
    minute = str(s % 3600 // 60)
    second = str(s % 3600 % 60)

    if "3" in second or "3" in minute or "3" in hour:
        count += 1

print(count)
