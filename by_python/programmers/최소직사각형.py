def solution(sizes):
    w = []
    h = []
    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            w.append(sizes[i][0])
            h.append(sizes[i][1])
        else:
            h.append(sizes[i][0])
            w.append(sizes[i][1])

    print(w)
    print(h)
    return max(w) * max(h)


if __name__ == "__main__":
    print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))