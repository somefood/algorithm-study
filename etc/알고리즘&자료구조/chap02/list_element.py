x = [1, 64, 1, 3.14, [32, 55], 'ABC']
for i in range(len(x)):
    print(f'x[{i}] = {id(x[i])}')