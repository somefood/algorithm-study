import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        dict = {}
        for s in strs:
            li = list(s)
            li.sort()
            anagram = ''.join(li)
            if anagram not in dict:
                dict[anagram] = list()
            dict[anagram].append(s)
        for v in dict.values():
            answer.append(v)
        return answer

    def book_solution_comprehension(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(s.book_solution_comprehension(["eat", "tea", "tan", "ate", "nat", "bat"]))
