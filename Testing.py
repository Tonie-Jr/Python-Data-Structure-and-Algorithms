from collections import defaultdict



class Solution:
    def group_Anagrams(self, strs:list) -> list[list[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())

List = ["rat", "art", "toni", "nito", "ball"]
two_solution = Solution()
print(two_solution.group_Anagrams(List))

print(ord("a"))
toni_list = [0] * 10
print(toni_list)

class Solution:
    def group_anagrams(self, strs:list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)]. append(s)
        return list(res.values())

List = ["rat", "art", "toni", "nito", "ball"]
two_solution = Solution()
print(two_solution.group_anagrams(List))

