class Solution:
    def topKFrequent(self, nums:list[int], K:int) -> list[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < K:
            res.append(arr.pop()[1])
        return res

my_list1, K = [4, 65, 6, 91, 91, 88, 86, 87, 86, 86, 2, 2, 2, 2, 432,], 3
topfrequent = Solution()
print(topfrequent.topKFrequent(my_list1, 3))