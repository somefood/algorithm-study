n = int(input())

answer = list(map(int, input().split()))
score = [0] * n

count = 1
for i in range(len(answer)):
    if answer[i] == 1:
        score[i] = count
        count += 1
    elif answer[i] == 0:
        score[i] = 0
        count = 1

print(sum(score))


