result = []
for i in range(1, 6):
    string = input()

    if "FBI" in string:
        result.append(i)

if len(result) <= 0:
    print("HE GOT AWAY!")
else:
    for i in result:
        print(i)

