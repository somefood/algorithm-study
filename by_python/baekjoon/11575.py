n = int(input())

alp = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
       "U", "V", "W", "X", "Y", "Z"]

for _ in range(n):
    a, b = map(int, input().split())
    plain = input()
    result = ""
    for s in plain:
        result += alp[(a * (ord(s) - 65) + b) % 26]
    print(result)
