import collections
from typing import Optional, List, Deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q: List = []

        if not head:
            return True

        node = head

        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
        return True

    def book_solution_deque(self, head: ListNode) -> bool:
        q: Deque = collections.deque()

        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        return True

    def book_solution_runner(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev


s = Solution()
link1 = ListNode()
link2 = ListNode()
link3 = ListNode()
link4 = ListNode()
link1.val = 1
link1.next = link2
link2.val = 2
link2.next = link3
link3.val = 2
link3.next = link4
link4.val = 1

print(s.isPalindrome(link1))
print(s.book_solution_deque(link1))
print(s.book_solution_runner(link1))
