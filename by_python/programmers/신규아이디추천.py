import re


def to_lower(string: str) -> str:
    return string.lower()


def remove_symbol(string: str) -> str:
    result = ""
    for s in string:
        if s.isalpha() or s.isnumeric():
            result += s
        elif s in ["-", "_", "."]:
            result += s
        else:
            continue
    return result


def remove_continuous_dot(string: str) -> str:
    return re.sub("\.{2,}", ".", string)


def remove_dot_first_last(string: str) -> str:
    if len(string) >= 1 and string[0] == ".":
        string = string[1:]
    if len(string) >= 1 and string[-1] == ".":
        string = string[:-1]
    return string


def add_if_len_zero(string: str) -> str:
    if len(string) == 0:
        return "a"
    return string


def cut_if_len_over_16(string: str) -> str:
    if len(string) >= 16:
        string = string[:15]
        if string[-1] == ".":
            return string[:-1]
    return string


def add_if_len_less_3(string: str) -> str:
    if len(string) <= 2:
        while len(string) < 3:
            string += string[-1]
        return string
    return string


def solution(new_id):
    answer = ''
    new_id = to_lower(new_id)

    new_id = remove_symbol(new_id)

    new_id = remove_continuous_dot(new_id)

    new_id = remove_dot_first_last(new_id)

    new_id = add_if_len_zero(new_id)

    new_id = cut_if_len_over_16(new_id)

    new_id = add_if_len_less_3(new_id)
    answer = new_id
    return answer


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))

"""
"...!@BaT#*..y.abcdefghijklm"	"bat.y.abcdefghi"
"""
