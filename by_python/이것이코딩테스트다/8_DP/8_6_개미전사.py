# 징수 N 을 입력 받기
n = int(input())
# 모든 식량 정 보 입력받기
array = list(map(int, input().split()))
# 앞서 계 산된 결 과를 저장하 기 위 한 DP 테이 블 초기 화
d = [0] * 100
# 다이나믹 프로그래밍 (Dynamic Programming) 진행(보텀업)
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

# 계산된 결과 출력
print(d[n - 1])

"""
4
1 3 1 5

6
1 3 26 99 1000 2
"""
