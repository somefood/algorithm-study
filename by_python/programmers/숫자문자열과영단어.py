def solution(s):
    answer = ""
    start = 0
    while start + 1 <= len(s):
        end = start

        while s[start:end] not in number_dict:
            end += 1
            if s[start:end].isdigit():
                answer += s[start:end]
                break

        if s[start:end] in number_dict:
            answer += number_dict[s[start:end]]
        start = end
    return int(answer)


# 개꿀 정답.. 그냥 replace 해주면 됨
def other_solution(s):
    answer = s
    num_s = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
             'nine': 9}

    for item in num_s.items():
        answer = answer.replace(item[0], str(item[1]))

    return int(answer)

number_dict = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

if __name__ == "__main__":
    print(solution("one4seveneight"))