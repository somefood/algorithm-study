t = int(input())

for i in range(t):
    n = int(input())
    p1_win, p2_win = 0, 0
    for j in range(n):
        p1, p2 = input().split()
        if p1 == "R" and p2 == "S":
            p1_win += 1
        elif p1 == "S" and p2 == "P":
            p1_win += 1
        elif p1 == "P" and p2 == "R":
            p1_win += 1
        elif p1 == "S" and p2 == "R":
            p2_win += 1
        elif p1 == "P" and p2 == "S":
            p2_win += 1
        elif p1 == "R" and p2 == "P":
            p2_win += 1
    if p1_win > p2_win:
        print("Player 1")
    elif p1_win < p2_win:
        print("Player 2")
    else:
        print("TIE")
