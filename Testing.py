
#Two sum Using the Hashmap technique. (One pass)
class Solution:
    def two_sum(self, nums:list[int], target:int) -> list[int]:
        prevdict = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevdict:
                return [prevdict[diff], i]
            prevdict[n] = i
        return []
List4, target = [3, 5, 64, 66, 744, 3], 130
two_solution = Solution()
print(two_solution.two_sum(List4, target))

# The two_sum the Hashmap approach. (two pass)
class Solution:
    def two_sum(self, nums:list[int], target:int) -> list[int]:
        indecies = {}
        for i, n in enumerate(nums):
            indecies[n] = i
        for i, n in enumerate(nums):
            diff = target - n
            if diff in indecies and indecies[diff] != i:
                return [i, indecies[diff]]
        return []

List4, target = [3, 5, 64, 66, 744, 3], 747
two_solution = Solution()
print(two_solution.two_sum(List4, target))
