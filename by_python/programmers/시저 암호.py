def solution(s, n):
    answer = ''

    for w in s:
        if w.isspace():
            answer += " "
        elif w.isupper():
            c = chr(65 + ((ord(w) + n) % 65 % 26))
            answer += c
        elif w.islower():
            c = chr(97 + ((ord(w) + n) % 97 % 26))
            answer += c
    return answer


# s = int()
# n = int(input())

print(solution("a B z", 4))

# print(ord('z') - 25)