# coding=utf-8
"""
문제 설명
rows행 columns열로 이루어진 격자가 있습니다. 처음에 모든 격자 칸 안에는 숫자 0이 쓰여 있습니다. 당신은 다음과 같은 과정을 통하여 격자에 숫자들을 채우고자 합니다.

현재 위치를 1행 1열로 정하고, 그 위치에 숫자 1을 씁니다.
r을 현재 위치의 행, c를 현재 위치의 열로 정의합니다.
만약 격자 내에 0이 쓰인 칸이 없거나, 더 이상 0이 쓰여 있는 칸에 다른 숫자를 쓸 수 없게 된다면 과정을 즉시 종료합니다.
만약 가장 최근에 쓴 숫자가 짝수라면, r행 c열에서 r+1행 c열로 이동합니다. r = rows라면, 1행으로 이동합니다.
만약 가장 최근에 쓴 숫자가 홀수라면, r행 c열에서 r행 c+1열로 이동합니다. c = columns라면, 1열로 이동합니다.
도착한 칸에 원래 쓰여 있던 수를 지우고 가장 최근에 쓴 숫자 + 1을 씁니다.
2번 과정으로 돌아갑니다.
정수 rows와 columns가 매개변수로 주어집니다. 주어진 과정을 따라 rows행 columns열로 이루어진 격자에 숫자를 썼을 때, 해당 격자를 2차원 정수 배열로 return 하도록 solution 함수를 완성해주세요.

제한사항
2 ≤ rows ≤ 1,000
2 ≤ columns ≤ 1,000
입출력 예
rows	columns	result
3	4	[[8,2,13,14],[16,10,4,15],[17,11,12,6]]
3	3	[[1,2,0],[0,3,4],[6,0,5]]
"""

def solution(rows, columns):
    answer = [[]]
    arr = [[0 for _ in range(columns)] for _ in range(rows)]
    num = 0
    r = -1
    c = 0

    while not check_if_no_exist_0(arr, rows, columns):
        if num % 2 == 0:
            r += 1
            if r == rows:
                r = 0
            arr[r][c] = num + 1
        else:
            c += 1
            if c == columns:
                c = 0
            arr[r][c] = num + 1

        num += 1

    return arr


def check_if_no_exist_0(arr, rows, columns):
    count = 0
    for i in range(rows):
        for j in range(columns):
            if arr[i][j] == 0:
                count += 1
    return True if count == 0 else False

print(solution(3, 4))
# print(solution(3, 3))
# print(solution(5, 5))