import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0

        for i, price in enumerate(prices):
            for j in range(i, len(prices)):
                max_price = max(prices[j] - price, max_price)

        return max_price

    def book_solution(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit


s = Solution()
# print(s.maxProfit([7, 1, 5, 3, 6, 4]))  # 5
# print(s.maxProfit([7, 6, 4, 3, 1]))  # 5
# print(s.maxProfit([2, 4, 1]))  # 5

print(s.book_solution([7, 1, 5, 3, 6, 4]))  # 5
# print(s.book_solution([7, 6, 4, 3, 1]))  # 5
# print(s.book_solution([2, 4, 1]))  # 5