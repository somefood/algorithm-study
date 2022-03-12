t = int(input())

for _ in range(t):
    split = input().split()
    mis, word = int(split[0]), split[1]

    result = ""
    for i in range(1, len(word) + 1):
        if mis == i:
            continue
        result += word[i-1]
    print(result)