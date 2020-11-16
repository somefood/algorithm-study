h = int(input())

count = 0
for i in range(h + 1): # h시간까지 포함
    for j in range(60): # 59분
        for k in range(60): # 59초
            if '3' in str(i)+str(j)+str(k):
                count += 1

print(count)

