# coding=utf-8
"""
문제 설명
정수 1, 2, 3을 담고 있는 배열이 주어집니다. 이 배열에 원소를 추가해서 배열 안의 1, 2, 3의 개수가 모두 같아지도록 하려 합니다. 단, 추가하는 원소의 개수는 최소가 되어야 합니다.

다음은 입출력 예제 1번의 배열을 나타낸 예시입니다.

[2, 1, 3, 1, 2, 1]
위 배열에 원소 2, 3, 3을 순서대로 추가하면 다음과 같이 바뀝니다.

[2, 1, 3, 1, 2, 1, 2, 3, 3]
원소 1, 2, 3의 개수가 모두 3개로 같아졌습니다. 세 개보다 적은 개수의 원소를 추가하여 1, 2, 3의 개수가 같도록 만드는 방법은 없으며, 추가해야 하는 원소는 1: 0개, 2: 1개, 3: 2개입니다.

정수 1, 2, 3을 담고 있는 배열 arr가 매개변수로 주어집니다. 원소 추가를 최소로 하여 배열 안의 1, 2, 3 각각의 개수가 모두 같도록 만들 때, 추가해야 하는 각 원소의 개수를 1, 2, 3 순서대로 배열에 담아 return 하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ arr의 길이 ≤ 100,000
arr의 원소는 1 또는 2 또는 3입니다.
입출력 예
arr	result
[2, 1, 3, 1, 2, 1]	[0, 1, 2]
[3, 3, 3, 3, 3, 3]	[6, 6, 0]
[1, 2, 3]	[0, 0, 0]
입출력 예 설명
입출력 예 #1

문제 예시와 같습니다.

입출력 예 #2

원소 1을 6개, 원소 2를 6개 추가하면 각 원소의 개수를 6개로 같게 만들 수 있습니다. 이보다 더 적은 수의 원소를 추가해서 배열 안의 1, 2, 3의 개수가 같도록 만드는 방법은 없습니다. 따라서 [6, 6, 0]을 return 합니다.

입출력 예 #3

이미 1, 2, 3의 개수가 모두 1개로 같기 때문에 원소를 추가하지 않아도 됩니다. 따라서 [0, 0, 0]을 return 합니다.
"""

def solution(arr):
    count_list = [0, 0, 0]
    answer = []

    for i in arr:
        if i == 1:
            count_list[0] += 1
        elif i == 2:
            count_list[1] += 1
        elif i == 3:
            count_list[2] += 1
        else:
            pass

    max_index = count_list.index(max(count_list))
    for i in range(3):
        if i == max_index:
            answer.append(0)
        else:
            answer.append(count_list[max_index] - count_list[i])

    return answer


print(solution([2, 1, 3, 1, 2, 1]))
print(solution([3, 3, 3, 3, 3, 3]))
print(solution([1, 2, 3]))