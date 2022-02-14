from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        print(s)

    def book_solution_two_pointer(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        print(s)

    def book_solution_slicing(self, s: List[str]) -> None:
        s[::-1]
        print(s)


s = Solution()
s.reverseString(["h", "e", "l", "l", "o"])
s.reverseString(["H", "a", "n", "n", "a", "h"])
s.book_solution_two_pointer(["H", "a", "n", "n", "a", "h"])
s.book_solution_slicing(["H", "a", "n", "n", "a", "h"])
