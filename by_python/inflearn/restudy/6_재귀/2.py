def preorder(v):
    if v > 7:
        return

    print(v, end=" ")
    preorder(v * 2)
    preorder(v * 2 + 1)


def inorder(v):
    if v > 7:
        return

    inorder(v * 2)
    print(v, end=" ")
    inorder(v * 2 + 1)


def postorder(v):
    if v > 7:
        return

    postorder(v * 2)
    postorder(v * 2 + 1)
    print(v, end=" ")


preorder(1)
print()
inorder(1)
print()
postorder(1)