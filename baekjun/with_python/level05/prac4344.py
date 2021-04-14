C = int(input())
for i in range(C):
    N, *score = map(int, input().split())
    avg = sum(score)/N
    over = [i for i in score if i > avg]
    result = len(over)/N*100
    print("{:.3f}%".format(result))