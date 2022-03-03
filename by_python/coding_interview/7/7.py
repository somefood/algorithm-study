from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def book_solution_with_in(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):

            complement = target - n

            if complement in nums[i + 1:]:
                return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]

    def book_solution_with_key1(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i

        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]

    def book_solution_with_key2(self, nums: List[int], target: int) -> List[int]:
            nums_map = {}
            for i, num in enumerate(nums):
                if target - num in nums_map:
                    return [nums_map[target - num], i]
                nums_map[num] = i

    def book_solution_two_pointer(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while not left == right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return [left, right]


s = Solution()
print(s.twoSum(nums=[2, 7, 11, 15], target=9))
print(s.book_solution_with_in(nums=[2, 7, 11, 15], target=9))
print(s.book_solution_with_key1(nums=[2, 7, 11, 15], target=9))
print(s.book_solution_with_key2(nums=[2, 7, 11, 15], target=9))
print(s.book_solution_two_pointer(nums=[2, 7, 11, 15], target=9))
