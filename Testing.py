from collections import defaultdict

import heapq

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


#METHODS IN PYTHON
#String manipulation
string = "i will be a Developer."
print(string.lower()) # Convert string into lowercase
print(string.upper()) # Convert string into uppercase
print(string.capitalize())# Convert the first Character in a string into a upper case
print(string.split()) # splits a string into substrings based on a delimiter and returns a list of these substrings.
print(string.find('z')) #Finds an element in a string. Returns the index position to the element
print(string.index('b')) #Finds an element in a string. Returns the index position to the element. Python find() produces -1 as output if it is unable to find the substring, whereas index() throws a ValueError exception.
print(string.count("e")) #counts the frequency of an element in a string.
print(string.replace("be", "become")) # Replace an element in a string with another.

#List Manipulation
List_m = ["Antony", 445, 5, ["Tonito", 4, 5, 3,5], 34]
List_n = [445, 5, 34, 65, 4,4,534, 5]
List_r = [44, 5, 3, 65, 4,4,54, 5]
List_s = ["Antony", "Tonito", "Anto", "Wachira", "Game", "Love"]
print(sorted(List_n))
List_r.sort()
print(List_r)
print(List_m.pop(3)[0])
print(List_m.pop(1))
print(List_m)
print(sorted(List_s))
List_s.remove('Antony')
print(List_s)

#Generate a password with secret and string
import string
import secrets

def password_generator(length = 15):
    alphabet = (
        string.punctuation + string.digits + string.ascii_letters
    )
    return ''.join(secrets.choice(alphabet)
                   for _ in range(length))
password = password_generator()
print(f"Your password is: {password}")


class Dict_testing:
    def dictionary_test(self, intergers: list[int]) -> list[int]:
        dict1 = {}
        for num in intergers:
            dict1[num] = dict1.get(num, 0) + 1
        return dict1[num]
my_list1 = [65, 765, 4, 6, 65]
Dicttest = Dict_testing()
print(Dicttest.dictionary_test(my_list1))

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
heaplist = [3, 65, 6,345, 7,66, 54, 234, 654, 66, 43, 23, 25, 325]
heapq.heapify(heaplist) #Transforms the list x into a heap, in-place, in linear time.
print(heaplist)
print(heapq.heappop(heaplist)) #ops and returns the smallest item from the heap, maintaining the heap property. Raises IndexError if the heap is empty.
print(heapq.heapreplace(heaplist, 44)) #Pops and returns the smallest item from the heap, then pushes the item onto the heap. The heap size remains the same.
print(heaplist)
print(heapq.heappush(heaplist, 400)) #Pushes the item onto the heap, maintaining the heap property.
print(heaplist)
print(heapq.heappushpop(heaplist, 500)) #Pushes the item onto the heap, then pops and returns the smallest item from the heap.
print(heapq.nlargest(2, heaplist)) #Returns a list with the n largest elements from the dataset defined by iterable. The key parameter can specify a function to extract a comparison key from each element.
print(heapq.nsmallest(3, heaplist)) #Returns a list with the n smallest elements from the dataset defined by iterable. The key parameter can specify a function to extract a comparison key from each element.