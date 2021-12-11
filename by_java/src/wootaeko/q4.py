# coding=utf-8
"""
문제 설명
처음과 끝이 이어져 있는 문자열을 상상해봅시다. 당신은 해당 문자열 내의 "같은 글자가 연속해 있는" 구간들을 추출하고자 합니다.

문자열 s가 매개변수로 주어집니다. s 내의 모든 "같은 글자가 연속해 있는" 구간의 길이를 각각 배열에 담아 오름차순으로 정렬하여 return 하도록 solution 함수를 완성해주세요.

제한사항
3 ≤ s의 길이 ≤ 1,000
s는 영어 소문자로 이루어진 문자열입니다.
입출력 예
s	result
"aaabbaaa"	[2,6]
"wowwow"	[1,1,2,2]
입출력 예 설명
입출력 예 #1

다음 애니메이션은 처음과 끝이 이어진 "aaabbaaa"의 각 구간을 구하는 과정을 나타낸 것입니다.
ex1

각 구간의 길이는 6("aaaaaa"), 2("bb")이므로, 이를 정렬한 [2,6]을 return 해야 합니다.
입출력 예 #2

다음 애니메이션은 처음과 끝이 이어진 "wowwow"의 각 구간을 구하는 과정을 나타낸 것입니다.
ex2

각 구간의 길이는 2("ww"), 1("o"), 2("ww"), 1("o")이므로, 이를 정렬한 [1,1,2,2]를 return 해야 합니다.
"""

def solution(s):
    answer = []
    length = len(s)
    mid = length // 2
    for i in range(mid):
        count = 0
        if s[i] == s[length - i - 1]:
            count += 2
    return answer


print(solution("aaabbaaa")) # [2, 6]
print(solution("wowwow")) # [1, 1, 2, 2]