from collections import defaultdict

def main():
  print("Hello from intro.py")
  # Creating an array (list in Python)
  arr = [1, 2, 3, 4, 5]

  # Accessing elements
  print(arr[0])  # Output: 1

  # Adding elements
  arr.append(6)
  print(arr)  # Output: [1, 2, 3, 4, 5, 6]

  # Removing elements
  arr.pop(2)  # Removes element at index 2
  print(arr)  # Output: [1, 2, 4, 5, 6]

  # Slicing
  sub_arr = arr[1:4] # Gets elements from index 1 to 3
  print(sub_arr)  # Output: [2, 4, 5]
  #Sort and Reverse function in array
  arr.sort()
  arr.reverse()

  #Noting index when traversing the list
  nums = [10, 20, 30, 40, 50]

  for index, num in enumerate(nums):
    print(f"Index: {index}, Value: {num}")

  # Hashing
  numList = [1,1,2,2,3,4,5,5]
  hashTable = {}
  for num in numList:
    if num in hashTable:
      hashTable[num] += 1
    else:
      hashTable[num] = 1
  print(hashTable)

  hashTable = defaultdict(int) # This creates a hashTable with value 0 for every key you can skip the initial step

  # you can also use hashTable.values() and hashTable.keys() to get the values and keys
  # if num in hashTable checks for key num in hashTable

  #hashTable.items() -> will display key and value pair in a tuple
  for i in hashTable.items():
    print(i)

  # Removing a record from hashTable
  my_dict = {"name": "Alice", "age": 25, "city": "New York"}

  # Remove a record by its key and get the value
  removed_value = my_dict.pop("age")
  print(removed_value)  # Output: 25
  print(my_dict)        # Output: {'name': 'Alice', 'city': 'New York'}
  
  #Sorting a hashTable acc to the values
  #Sorted returns a list so, dict() is needed and item[1] is for sorting the values, item[0] is for sorting 
  #the keys, use rverse = True for descending order sorting
  sortedHashTable = dict(sorted(hashTable.items(), key= lambda item: item[1]))
  print(f"sortedHashTable(Asc) : {sortedHashTable}")

  sortedHashTable = dict(sorted(hashTable.items(), key= lambda item: item[1], reverse=True))
  print(f"sortedHashTable(Des) : {sortedHashTable}")

  # Creating a set
  unique_nums = {1, 2, 3, 3, 4}
  print(unique_nums)  # Output: {1, 2, 3, 4}

  # Adding and removing elements
  unique_nums.add(5)
  unique_nums.remove(3)
  print(unique_nums)

  # set operations
  set1 = {1, 2, 3}
  set2 = {3, 4, 5}

  # IMP
  # in python, lookup for a element in a arr in n time but in a set it's o(1)
  # because set(Hashset) uses a internal hashtable
  # if you want to access 5 in const time, convert list to a set and do that

  if 1 in set1:
    print("1 is there")

  # Union
  print(set1 | set2)  # Output: {1, 2, 3, 4, 5}

  # Intersection
  print(set1 & set2)  # Output: {3}

  # Difference
  print(set1 - set2)  # Output: {1, 2}

  # Prefix Sum Pattern
  #This pattern happens when you find the cuminlative sum of the array from 1 to n
  #arr is [1,2,3,4,5] prefix sum arr is [1,3,6,10,15]

  arr = [1,2,3,4,5]
  prefixSumArr = list(arr)
  for i in range(1,len(arr)):
    prefixSumArr[i] = prefixSumArr[i-1] + prefixSumArr[i]
  print("Prefix Sum Arr: ", prefixSumArr)

  # Varition of this pattern is to use postfix and prefix mul arrs -> depends on the problem

  # You can use this to find sum of index a to index b easily = prefixSumArr[b] - prefixSumArr[a-1]
  # When the a is 0, it's equal to prefixSumArr[b] only
  # O(n+q) q queries is given (a1,b1)....(aq,bq) and array size is n
  # n time to form the prefix sum array and q time to run the through the inputs so ,its O(n+q)

  # When you want a hashtable of count of each char in a string
  # Shortcut to make a hashMap
  example_string = "Hello"
  Array = [1,2,2,3,3,3,4,4,1,0,67]
  from collections import Counter
  hashMap = Counter(example_string)
  hashMap2 = Counter(Array)
  print("Hash Map1: ", hashMap)
  print("Hash Map1: ", hashMap2)

  #Strings
  s = "zebra"
  for i in s:
    print(i)
  list1 = list(s)
  print(list1)

  #Sorting a string
  list2 = sorted(s) # TAKES A STRING AND RETURNS A LIST
  print("".join(list2)) # TAKES A LIST of STRINGS AND RETURNS A STRING
  # JOIN CAN BE ONLY USED ON LIST OF STRINGS

  # CODING TRICKS
  # for while loop, when you can't think of a exit condn
  # Put the if codn inside the while as the exit codn for while -> coding will become easy

  #Slicing shortcuts
  # Define a sample list
  arr = [10, 20, 30, 40, 50, 60, 70]

  # 1. Slice the entire list
  print(arr[:])  
  # Output: [10, 20, 30, 40, 50, 60, 70]
  # Explanation: This creates a shallow copy of the list (everything is included).

  # 2. Slice from the beginning up to a certain index
  print(arr[:4])  
  # Output: [10, 20, 30, 40]
  # Explanation: Slices from the start (index 0) to index 4 (exclusive).

  # 3. Slice from a certain index to the end
  print(arr[3:])  
  # Output: [40, 50, 60, 70]
  # Explanation: Slices from index 3 to the end of the list.

  # 4. Slice between two indices
  print(arr[2:5])  
  # Output: [30, 40, 50]
  # Explanation: Slices from index 2 to index 5 (exclusive).

  # 5. Use a step to skip elements
  print(arr[::2])  
  # Output: [10, 30, 50, 70]
  # Explanation: Slices the entire list but skips every other element (step = 2).

  # 6. Reverse the entire list
  print(arr[::-1])  
  # Output: [70, 60, 50, 40, 30, 20, 10]
  # Explanation: Steps through the list in reverse (negative step).

  # 7. Reverse a subset of the list
  print(arr[5:2:-1])  
  # Output: [60, 50, 40]
  # Explanation: Slices from index 5 to index 2 (exclusive), moving backward.

  # 8. Slice the last `k` elements
  k = 3
  print(arr[-k:])  
  # Output: [50, 60, 70]
  # Explanation: Slices the last 3 elements using negative indexing.

  # 9. Slice up to the last element
  print(arr[:-1])  
  # Output: [10, 20, 30, 40, 50, 60]
  # Explanation: Slices all elements except the last one.

  # 10. Empty slice (when start > stop or out-of-bound indices)
  print(arr[5:1])  
  # Output: []
  # Explanation: An empty slice as the start index (5) is greater than the stop index (1).

  # 11. Skip and reverse combined
  print(arr[::-2])  
  # Output: [70, 50, 30]
  # Explanation: Reverses the list and skips every other element.

  # 12. Out-of-bounds slicing
  print(arr[10:15])  
  # Output: []
  # Explanation: When the indices are out of bounds, Python safely returns an empty list.



if __name__ == "__main__":
  main()