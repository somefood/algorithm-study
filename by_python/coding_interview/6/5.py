from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        dict = {}
        for s in strs:
            li = list(s)
            li.sort()
            anagram = ''.join(li)
            print(anagram)
            if anagram not in dict:
                dict[anagram] = list()
            dict[anagram].append(s)
        for v in dict.values():
            answer.append(v)
        return answer


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
