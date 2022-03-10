T = int(input())

for _ in range(T):
    N = int(input())
    total_c = 0.0
    total_g = 0.0
    for _ in range(N):
        C, G = map(float, input().split())
        total_c += C
        total_g += C * G

    GPA = total_g / total_c
    print(int(total_c), '%.1f' % GPA)