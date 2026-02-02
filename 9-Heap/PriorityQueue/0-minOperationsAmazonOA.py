# Problem Statement:
# The manager of an Amazon warehouse needs to ship `n` products from different locations.
# The location of the `i-th` product is represented by an array `locations[i]`.
# The manager is allowed to perform one operation at a time.
#
# Operations:
# 1. If there are at least two products in the inventory, the manager can pick two products 
#    (x and y) and ship them together *only if* they have different locations.
# 2. If only one product is left, it must be shipped alone.
#
# After shipping, the products are removed from inventory, and the order of remaining 
# products stays the same.
#
# Given an array `locations` representing product locations, determine the minimum number 
# of operations required to ship all products.
#
# Example Test Case:
# Input: 
# locations = [1, 2, 2, 3, 3, 3]
# Output:
# 3
#
# Explanation:
# - Ship (3,2) → Remaining: [1, 2, 3, 3]
# - Ship (3,1) → Remaining: [2, 3]
# - Ship (3,2) → Remaining: []
# - Total operations = 3

import heapq
from collections import Counter
def minOperations(locations):
  # hashTable = {}
  # for location in locations:
  #   if location not in hashTable:
  #     hashTable[location] = 0
  #   hashTable[location] += 1
  
  hashTable = Counter(locations)

  location_freq = hashTable.values()
  result = []

  for freq in location_freq:
    heapq.heappush(result, -freq)

  operations = 0
  while len(result) > 1:
    location1 = -heapq.heappop(result)
    location2 = -heapq.heappop(result)

    location1-=1
    location2-=1
    operations+=1

    if location1 != 0:
      heapq.heappush(result, -location1)
    if location2 != 0:
      heapq.heappush(result, -location2)

  if result:
    operations += (-heapq.heappop(result))
  
  return operations

test_cases = [
    # Test Case 1: Basic case with different locations
    ([1, 2, 2, 3, 3, 3], 3),  
    # Expected Output: 3
    # Explanation: (3,2) -> (3,1) -> (3,2)

    # Test Case 2: All products from the same location (worst case)
    ([1, 1, 1, 1, 1], 5),
    # Expected Output: 5
    # Explanation: Must ship one by one

    # Test Case 3: All products from different locations (best case)
    ([1, 2, 3, 4, 5, 6, 7, 8], 4),
    # Expected Output: 4
    # Explanation: Always pair two different locations

    # Test Case 4: Large input with mixed repetition
    ([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5], 8),
    # Expected Output: 8
    # Explanation: Greedy pairing minimizes operations

    # Test Case 5: Single product (edge case)
    ([1], 1),
    # Expected Output: 1
    # Explanation: Must ship alone

    # Test Case 6: Two products, same location
    ([2, 2], 2),
    # Expected Output: 2
    # Explanation: Must ship separately

    # Test Case 7: Two products, different locations
    ([1, 2], 1),
    # Expected Output: 1
    # Explanation: Ship together

    # Test Case 8: Large number of products with various groupings
    ([i % 50 for i in range(1000)], 500),
    # Expected Output: 500
    # Explanation: Every two products can be shipped together
]

# Test Runner
def run_tests(func):
    for i, (locations, expected) in enumerate(test_cases):
        result = func(locations)
        print(f"Test Case {i+1}: {'PASS' if result == expected else 'FAIL'} (Expected: {expected}, Got: {result})")


run_tests(minOperations)  





  