# 파이썬 리스트 사용
# class Stack(list):
#     push = list.append
#
#     def is_empty(self):
#         if not self:
#             return True
#         else:
#             return False
#
#     def peek(self):
#         return self[-1]


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if not self.head:
            return True
        return False

    def push(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return None

        ret_data = self.head.data

        self.head = self.head.next

        return ret_data

    def peek(self):
        if self.is_empty():
            return None

        return self.head.data


if __name__=="__main__":
    s = Stack()
    print(s.is_empty())

    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)

    print("peek of data: {}".format(s.peek()))

    while not s.is_empty():
        print(s.pop())