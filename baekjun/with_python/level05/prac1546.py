N = int(input())
score = [int(i) for i in input().split()]
M = max(score)

score = [i/M*100 for i in score]
print(sum(score)/N)