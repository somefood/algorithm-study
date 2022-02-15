class Solution:
    def longestPalindrome(self, s: str) -> str:
        left = 0

        while True:
            right = len(s) - 1
            print(right)
            while left < right:
                print(left, right)
                if s[left] == s[right]:
                    word = s[left:right + 1]
                    if s[left:right + 1] == s[right:left:-1]:
                        return s[left:right + 1]
                else:
                    right -= 1
            left += 1

    def book_solution_two_pointer(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]

        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        for i in range(len(s) - 1):
            result = max(result,
                         expand(i, i + 1),
                         expand(i, i + 2),
                         key=len)
        return result


s = Solution()
# print(s.longestPalindrome("babad"))
# print(s.longestPalindrome("cbbd"))
print(s.book_solution_two_pointer("babad"))
print(s.book_solution_two_pointer("cbbd"))
