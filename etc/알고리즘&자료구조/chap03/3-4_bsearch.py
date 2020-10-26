from typing import Any, Sequence


def bin_search(a: Sequence, key: Any) -> int:
    pl = 0
    pr = len(a) - 1

    while True:
        pc = (pl + pr) // 2
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc+1
        else:
            pr = pc-1
        if pl > pr:
            break
    return -1


if __name__ == '__main__':
    x = [1, 2, 3, 5, 7, 8, 9]
    ky = 7
    idx = bin_search(x, ky)

    if idx == -1:
        print('X')
    else:
        print(idx)