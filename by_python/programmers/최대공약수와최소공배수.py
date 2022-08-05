# 최대 공약수는 a, b 재귀로 왔다갔다
# 최소 공배수는 a * b한 값을 최대 공약수로 나누면 됨

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


def solution(n, m):
    answer = []
    gcd_value = gcd(max(n, m), min(n, m))
    lcd_value = (n * m) // gcd_value
    answer.append(gcd_value)
    answer.append(lcd_value)
    return answer


if __name__ == "__main__":
    print(solution(3, 12))
    print(solution(2, 5))