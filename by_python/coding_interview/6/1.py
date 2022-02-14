import collections
import re
from typing import Deque


class Solution:
    def isPalindrome(self, word: str) -> bool:
        strs = []
        for s in word:
            if s.isalnum():
                strs.append(s.lower())

        length = len(strs)
        for i in range(length // 2):
            if strs[i] != strs[length - 1 - i]:
                return False
        return True

    def book_solution(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        return True

    def book_solution_with_deque(self, s: str) -> bool:
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True

    def book_solution_with_slicing(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]



s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))
print(s.book_solution("A man, a plan, a canal: Panama"))
print(s.book_solution("race a car"))
print(s.book_solution_with_deque("A man, a plan, a canal: Panama"))
print(s.book_solution_with_deque("race a car"))
print(s.book_solution_with_slicing("A man, a plan, a canal: Panama"))
print(s.book_solution_with_slicing("race a car"))