from itertools import combinations, permutations


def solution(nums):
    answer = 0
    i = len(nums) // 2
    s = len(set(nums))
    return i if i < s else s


print(solution([3, 1, 2, 3]))
print(solution([3, 3, 3, 2, 2, 4]))
