plain = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
crypt = "DEFGHIJKLMNOPQRSTUVWXYZABC"

word = input()

for s in word:
    print(plain[crypt.index(s)], end="")