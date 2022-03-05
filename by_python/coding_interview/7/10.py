from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum([nums[i] for i in range(len(nums)) if i % 2 == 0])

    def book_solution_pythonic(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])


s = Solution()
print(s.arrayPairSum([1, 4, 3, 2]))
print(s.book_solution_pythonic([1, 4, 3, 2]))
