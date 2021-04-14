N = int(input())
for i in range(N):
    ox = input()
    inc = 0
    score = 0
    for j in range(len(ox)):
        if j <= 0:
            if ox[j] == "O":
                inc += 1
                score += inc
        else:
            if ox[j] == "O":
                if ox[j] == ox[j-1]:
                    inc += 1
                    score += inc
                else:
                    inc = 1
                    score += inc
            else:
                inc = 0
    print(score)