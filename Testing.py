from collections import defaultdict


class Solution:
    def two_sum(self, strs:list) -> list[list[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())

List = ["rat", "art", "toni", "nito", "ball"]
two_solution = Solution()
print(two_solution.two_sum(List))
