# 세 정수를 입력받아 최대갓값 구하기

a, b, c, *args = map(int, input('세 정수 입력해주세요').split())
maximum = a

if b > maximum: maximum = b
if c > maximum: maximum = c

print(f"최대값은 {maximum}입니다.")