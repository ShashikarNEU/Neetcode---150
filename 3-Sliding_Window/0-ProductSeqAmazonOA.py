# Problem Statement: Valid Product Code Substrings
# Given: A string s (product codes) where characters are in 'a'-'g'.
# Valid Substring Definition: A substring is valid if for every character in it:
# (count of that character) ≤ (number of distinct characters in the substring).
# Task: Count all valid substrings in s

# Example: s = "abaa"
# Valid Substrings:
# Length 1:

# "a" (at index 0): 'a' appears 1 time, distinct chars = 1 → Valid.

# "b" (at index 1): 'b' appears 1 time, distinct chars = 1 → Valid.

# "a" (at index 2): 'a' appears 1 time, distinct chars = 1 → Valid.

# "a" (at index 3): 'a' appears 1 time, distinct chars = 1 → Valid.

# Length 2:

# "ab" (s[0:2]):

# Counts: {'a':1, 'b':1}, distinct chars = 2.

# Check: max(1,1) ≤ 2 → Valid.

# "ba" (s[1:3]):

# Counts: {'b':1, 'a':1}, distinct chars = 2 → Valid.

# "aa" (s[2:4]):

# Counts: {'a':2}, distinct chars = 1.

# Check: 2 ≤ 1 → Invalid.

# Length 3:

# "aba" (s[0:3]):

# Counts: {'a':2, 'b':1}, distinct chars = 2.

# Check: max(2,1) ≤ 2 → Valid.

# "baa" (s[1:4]):

# Counts: {'b':1, 'a':2}, distinct chars = 2.

# Check: max(1,2) ≤ 2 → Valid.

# Length 4:

# "abaa" (s[0:4]):

# Counts: {'a':3, 'b':1}, distinct chars = 2.

# Check: max(3,1) ≤ 2 → Invalid.

# Total Valid Substrings: 6
# ("a", "b", "a", "a", "ab", "ba", "aba", "baa" → Valid = 6, Invalid = 2).

def product_seq(seq):
  n = len(seq)
  valid_substring = 0
  for i in range(n):
    unique_count = 0
    hashTable = {}
    for j in range(i,n):
      char = seq[j]

      if char not in hashTable:
        unique_count+=1
        hashTable[char] = 0
      
      hashTable[char] += 1

      max_value = max(hashTable.values())

      if max_value <= unique_count:
        valid_substring += 1
      else:
        break # it becomes invalid from this point
      
  return valid_substring

# Code for all sub strings
# abc
# Sub string generation acc to the loops
# a,ab,abc
# b, bc
# c
def write_all_substrings(seq):
  result = []
  for i in range(len(seq)):
    for j in range(i, len(seq)):
      sub_string = seq[i:j+1]
      result.append(sub_string)
  return result





