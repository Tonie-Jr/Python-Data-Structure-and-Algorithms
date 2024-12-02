#ARRAYS AND HASHING
# @1 Contains Duplicate
class Solution:
    def hasDuplicate1(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
nums1 = [1,3,6,3,6,8,7,7]
solution1 = Solution()
print(solution1.hasDuplicate1(nums1))

#Has Duplicate using the sorting approach
class Solution:
    def hasDuplicate2(self, nums:list[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False

my_list = [3,4,6,4,4,7,5,3,35,66,4,3]
solution2 = Solution()
print(solution2.hasDuplicate2(my_list))


#@1 Contains duplicate but an efficient method.
class Solution():
    def hasDuplicate3(self, nums: list[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
nums2 = [45,34,6,32,77,54,77,65]
solution2 = Solution()
print(solution2.hasDuplicate3(nums2))



class Fruit:
     def __init__(self, name, color):
         self.name = name
         self.color = color
my_fruit = Fruit("Apple", "green")
print(f"I love {my_fruit.color} {my_fruit.name}")

class Person:
    origin = "Kenya"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfucn(self):
        print(f"My name is {self.name}, I'm {self.age} years old, and I come from {Person.origin}.")
p1 = Person("Antony", 29)
print(p1.name)
print(p1.age)
p1.myfucn()

#class inheritance
class car:
    def __inti__(self, make, model, year):
        self.name = make
        self.mode = model
        self.year = year

class Electrical(car):
    def __init__(self, make, model, year, battery_size):
        super().__inti__(make, model, year)
        self.battery_size = battery_size
    def charge_battery(self):
        print("The battery is charging")

my_car = Electrical("Audi", "R8", 2018, "Medium")

list1 = [1, 2, 3, 4, 5, 65, 43, 66, 75]
print(len(list1))

#Anagram. Anagram is a string that contains exact same characters as another character but the order of characters can be different

class check:
    def anagrams(self, s: str, r: str) -> bool:
        if sorted(r) != sorted(s):
            return False
        return True
r,s = "toni", "nito"
solution3 = check()
print(f"It is {solution3.anagrams(r,s)} strings r and s are anagrams.")

#Are Anagrams
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

Name1, Name2 = "Antony", "Antonio"
solution = Solution()
print(solution.isAnagram(Name1, Name2))
countsW = { "Name" : "Antony" }
print(len(countsW["Name"]))


#Two sum Sorting
class Solution:
    def twosum(self, nums:list[int], target: int) -> list[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])
        A.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            cur = A[i][0] + A[j][0]
            if cur == target:
                return[min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]
            elif cur > target:
                j -= 1
            else:
                i += 1
        return []

List2, target2 = [1,2,5,8,3], 5
twosum_solution = Solution()
print(twosum_solution.twosum(List2, target2))

#Two sum Bruteforce.
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
List3, target = [3, 5, 64, 66, 744, 3], 130
Tow_solution = Solution()
print(Tow_solution.twoSum(List3, target))

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

