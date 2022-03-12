arr = []
for _ in range(5):
    arr.append(int(input()))

burger = arr[0:3]
beverage = arr[3:]

print(min(burger) + min(beverage) - 50)