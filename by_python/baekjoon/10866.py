import sys

N = int(sys.stdin.readline())

deque = []

for i in range(N):
    cmd = sys.stdin.readline().split()

    c = cmd[0]

    data = 0

    if c == "push_front":
        data = int(cmd[1])
        deque.insert(0, data)
    elif c == "push_back":
        data = int(cmd[1])
        deque.insert(len(deque), data)
    elif c == "pop_front":
        if len(deque) <= 0:
            data = -1
        else:
            data = deque.pop(0)
        print(data)
    elif c == "pop_back":
        if len(deque) <= 0:
            data = -1
        else:
            data = deque.pop()
        print(data)
    elif c == "size":
        print(len(deque))
    elif c == "empty":
        if len(deque) <= 0:
            data = 1
        else:
            data = 0
        print(data)
    elif c == "front":
        if len(deque) <= 0:
            data = -1
        else:
            data = deque[0]
        print(data)
    elif c == "back":
        if len(deque) <= 0:
            data = -1
        else:
            data = deque[-1]
        print(data)
