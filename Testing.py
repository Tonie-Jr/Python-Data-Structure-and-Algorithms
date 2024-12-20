import heapq


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

class Solution:
    def topkFrequent(self, nums: list[int], k:int)-> list[int]:
        count1 = {}
        for num in nums:
            count1[num] = 1 + count1.get(num, 0)

        heap = []
        for num in count1.keys():
            heapq.heappush(heap, (count1[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

List5, k = [3, 54, 55,54, 66,55, 6, 6, 6, 76, 76, 76, 76, 66], 3
Topkfrequent = Solution()
print(Topkfrequent.topkFrequent(List5, k))
