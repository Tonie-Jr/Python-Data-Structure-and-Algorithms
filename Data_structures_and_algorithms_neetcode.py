#ARRAYS AND HASHING
# @1 Contains Duplicate
from operator import length_hint
from shelve import Shelf


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

q = {"Name": "Antony", "Age": 29}
print(q.get("Name"))
print(q.keys()) # Return a list of all the keys in dictionary.
print(q.values()) #Return a list of all values in a dictionary.
print(q.update({"Height": 6})) #Update a dictionary with a specified key value
print(q.items()) #Convert the key values as tuples and return an iterable (list)
print(q.setdefault("PIN", 573893)) #Returns the value of the key specified. If the key is not present, then adds the key (1st argument) and the value (argument) provided through this method.
print(q.pop("Name")) #Remove the value and key whose keys are passed in the argument
t = { "name": "Tonito", "Hobby": "Football"}
print(t.popitem()) # Remove the last inserted key value pair and return it as a tuple
print(q.clear()) # Remove all items in a dictionary

#Working wing Heap
import heapq
heaplist = [3, 65, 6,345, 7,66, 54, 234, 654, 66, 43, 23, 25, 325]
heapq.heapify(heaplist) #Transforms the list x into a heap, in-place, in linear time.
print(heaplist)
print(heaplist[:])
print(heapq.heappop(heaplist)) #ops and returns the smallest item from the heap, maintaining the heap property. Raises IndexError if the heap is empty.
print(heapq.heapreplace(heaplist, 44)) #Pops and returns the smallest item from the heap, then pushes the item onto the heap. The heap size remains the same.
print(heaplist)
print(heapq.heappush(heaplist, 400)) #Pushes the item onto the heap, maintaining the heap property.
print(heaplist)
print(heapq.heappushpop(heaplist, 500)) #Pushes the item onto the heap, then pops and returns the smallest item from the heap.
print(heapq.nlargest(2, heaplist)) #Returns a list with the n largest elements from the dataset defined by iterable. The key parameter can specify a function to extract a comparison key from each element.
print(heapq.nsmallest(3, heaplist)) #Returns a list with the n smallest elements from the dataset defined by iterable. The key parameter can specify a function to extract a comparison key from each element.
l1 = [3, 54, 6, 5, 4 , 6, 7, 67, 888, 76, 7, 467]
# Max heap
heapq._heapify_max(l1) # Returns the list max heap where the root of the heap is the largest element in the list.
negated_l1 = [-x for x in l1] #Negate the list so that we can do max heap
heapq.heapify(negated_l1)#Heapifies the list and returns a max heap.
print(negated_l1)

print(l1)
l2 = [35,55, 66, 67, 88, 92, 91]
heapified = heapq.merge(l1, l2) #Merges the two lists and returns heapfied list.
print(list(heapified))


#The Top k frequent elements. Given an integer array nums and an integer k, return the k most frequent elements within the array.

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
    def topkFrequent(self, nums: list[int], k: int) -> list[int]:
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


List5, k = [3, 54, 55, 54, 66, 55, 6, 6, 6, 76, 76, 76, 76, 66], 3
Topkfrequent = Solution()
print(Topkfrequent.topkFrequent(List5, k))

class Dog:
    Species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

dog1 = Dog("Bobby", 3)  # Creating an object
print(dog1.name)  # printing the Object's name.
print(dog1.age)  # printing the object's age.


class Dog:
    Species = "Canine" #Class attribute
    def __init__(self, name, age):
        self.name = name # Instance attribute
        self.age = age # Instance attribute

    def __str__(self):
        return f"{self.name} is {self.age} years old." #Correct: returning of a string.

dog1 = Dog("Bobby", 3) #Creating an object
dog2 = Dog("Charlie", 5) #Creating an object
print(dog1) #printing the Object.
print(dog2) #printing the object.


class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        pass
class Dog1(Animal): #Child inheriting from the parent class Animal.
    def speak(self):
        return f"{self.name} barks"
dog = Dog1("Buddy")
print(dog.speak())

class Person(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def Display(self):
        print(self.name, self.id)

class Emp(Person):
    def Print(self):
        print()

employee_details = Emp("Antony", 5432345)
print(employee_details.Print())

# Polymorphism and inheritance
class Shapes:
    def area(self):
        return "Undefined"

class Rectangle(Shapes):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.142 * self.radius**2

shapes = [Rectangle(45, 64), Circle(56)]
for shape in shapes:
    print(f"Area: {shape.area()} ")


class Animal:
    def sound(self):
        return "Make some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

animals = [Dog(), Cat(), Animal()] #Polymorphic behavior.
for animal in animals:
    print(animal.sound()) # Call the override method based on the object behaviour.

#Python Data Abstraction
from abc import ABC, abstractmethod #Importing ABC and abstract method
class Car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    @abstractmethod
    def PrintDetails(self): #Creating an abstract method
        pass

    def accelerate(self): #Creating a concrete method
        print("speed up...")
    def breaks_applied(self):
        print("Car stopped")

class Hatchback(Car): #Creating a child class
    def PrintDetails(self):
        print("Brand: ", self.brand)
        print("Model: ", self.model)
        print("Year :", self.year)

    def sunroof(self):
        print("Not having this feature.")

class Suv(Car): #Creating a child class
    def PrintDetails(self):
        print("Brand: ", self.brand)
        print("Model: ", self.model)
        print("Year :", self.year)

    def sunroof(self):
        print("Available")

car1 = Hatchback("Maruti", "Alto", "2022")
print(car1.PrintDetails())
print(car1.sunroof())


car2 = Suv("Mazda", "cx 5", "2025")
print(car2.PrintDetails())
print(car2.sunroof())

# The Flower Spiral
import turtle
import colorsys
turtle.speed(0)
turtle.bgcolor("black")
h = 0
for i in range(16):
    for j in range (18):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        turtle.color(c)
        h += 0.005
        turtle.right(90)
        turtle.circle(150 - j * 6, 90)
        turtle.left(90)
        turtle.circle(150 - j * 6, 90)
        turtle.right(180)
    turtle.circle(40, 24)
turtle.done()

from turtle import *
sides = 3
colors = ["#FF00B8", "#00B8FF", "#B8FF00"]  # Removed the comment symbol (#) inside the list
tracer(5)  # This sets the update frequency for turtle graphics
speed(1)  # Removed `turtles`, since `speed` is a method of the `turtle` module
delay(0)  # Removed `turtles`, as `delay` is also part of the `turtle` module
bgcolor("black")  # Sets the background color
for i in range(500):
    color(colors[i % len(colors)])  # Cycles through the colors in the list
    fd(i * 3 // sides + 1)  # Forward movement
    lt(360 / sides + 1)  # Left turn
    width(i * sides / 250)  # Dynamic line width
done()  # Ends the turtle graphics program



from turtle import *
t = [Turtle(), Turtle()]
c = [1, 3]
colors = ["#F24452", "#542D59", "#F2CF63" ]
bgcolor("black")
tracer(30)
ht()

for index, i in enumerate(t):
    i.ht()
    i.width(3)
    i.pu()
    i.seth(90)
    i.bk(120 * (c[index]))
    i.seth(0)
    i.pd()
for i in colors:
    t[0].color(i)
    t[1].color(i)
    color(i)
    for _ in range(361):
        for _ in range (12):
            t[0].fd(2)
            t[0].lt(1)
        pu()
        goto(t[0].pos())
        t[1].fd(c[1] * 2)
        t[1].lt(1)
        pd()
        goto(t[1].pos())
done()

