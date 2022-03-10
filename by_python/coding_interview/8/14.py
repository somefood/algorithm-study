from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1


s = Solution()
link1 = ListNode()
link2 = ListNode()
link3 = ListNode()
link1.val = 1
link1.next = link2
link2.val = 2
link2.next = link3
link3.val = 4

link4 = ListNode()
link5 = ListNode()
link6 = ListNode()
link4.val = 1
link4.next = link5
link5.val = 3
link5.next = link6
link6.val = 4

print(s.mergeTwoLists(link1, link4))