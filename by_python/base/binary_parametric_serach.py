"""
- 파라메트릭 서치란 최적화 문제를 결정 문제("예" 혹은 "아니오")로 바꾸어 해결하는 기법
    - ex) 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
- 코테에서 파라메트릭 서치 문제는 이진 탐색을 이용하여 해결할 수 있다.
"""


n, m = map(int, input().split())

array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid

    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)

"""
4 6
19 15 10 17
"""