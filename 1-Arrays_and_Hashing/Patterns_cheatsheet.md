# Arrays & Hashing - Pattern Revision List

Quick revision before interviews. Read the pattern, recall the trick, move on.
n = input size unless mentioned otherwise.

---

## 1. Two Sum
- **Pattern:** Hash Table (complement lookup)
- **LeetCode:** https://leetcode.com/problems/two-sum/
- **Neetcode:** https://neetcode.io/solutions/two-sum
- **Idea:** a + b = target, so for every num check if `target - num` already exists in the hashTable. If yes -> answer. The trick is to add num to the table AFTER checking, else you pick the same element twice (think `[3,2,4]` target 6).
- **TC:** O(n) | **SC:** O(n)

---

## 2. Contains Duplicate (217)
- **Pattern:** Hash Set / Hash Table (seen before?)
- **LeetCode:** https://leetcode.com/problems/contains-duplicate/
- **Neetcode:** https://neetcode.io/solutions/contains-duplicate
- **Idea:** Keep a set of seen nums. If the num is already there -> duplicate -> return True. Simple "have I seen this before" pattern.
- **TC:** O(n) | **SC:** O(n)

---

## 3. Valid Anagram (242)
- **Pattern:** Hash Table (frequency count)
- **LeetCode:** https://leetcode.com/problems/valid-anagram/
- **Neetcode:** https://neetcode.io/solutions/valid-anagram
- **Idea:** Anagram = same letters same count. Build a freq hashTable for both strings and just compare them. Brute force is sort both and equate -> O(nlogn).
- **TC:** O(m+n) | **SC:** O(1) -> only 26 letters max so table stays small

---

## 4. Group Anagrams (49)
- **Pattern:** Hash Table with a built key
- **LeetCode:** https://leetcode.com/problems/group-anagrams/
- **Neetcode:** https://neetcode.io/solutions/group-anagrams
- **Idea:** All anagrams share the same key. Brute force key = sorted string (O(mnlogn)). Optimal key = freq array of 26 letters turned into a `tuple` (tuple bcz dict keys can't be a list). Group all strings under that key.
- **TC:** O(m*n) | **SC:** O(m) -> m = no of strings, n = longest string

---

## 5. Top K Frequent Elements (347)
- **Pattern:** Bucket Sort (count as index)
- **LeetCode:** https://leetcode.com/problems/top-k-frequent-elements/
- **Neetcode:** https://neetcode.io/solutions/top-k-frequent-elements
- **Idea:** Brute force = freq map then sort by value -> O(nlogn). Optimal = bucket sort. Make an array where the INDEX is the count, value is the list of nums with that count. A num can repeat at most n times so array size = n+1. Read from the back to get top k.
- **TC:** O(n) | **SC:** O(n)

---

## 6. Product of Array Except Self (238)
- **Pattern:** Prefix & Postfix product
- **LeetCode:** https://leetcode.com/problems/product-of-array-except-self/
- **Neetcode:** https://neetcode.io/solutions/products-of-array-except-self
- **Idea:** no division allowed. Form a prefix arr and a postfix arr, then `result[i] = pre[i-1] * post[i+1]`. Mind the boundary condns -> if `i-1 < 0` use 1, if `i+1 > len-1` use 1.
- **SC O(1):** use the input arr as the prefix arr and the result arr as the postfix arr, then write the answer into the result arr.
- **TC:** O(n) | **SC:** O(1) extra (output arr not counted)

---

## 7. Valid Sudoku (36)
- **Pattern:** Hash Set (3 separate duplicate checks)
- **LeetCode:** https://leetcode.com/problems/valid-sudoku/
- **Neetcode:** https://neetcode.io/solutions/valid-sudoku
- **Rules:** no duplicate number in any row, any col, any 3x3 box. Use a set to catch repeats. Ignore the `.` cells.
- **Idea:** first two checks (rows, cols) are easy -> one set per row, one set per col, if num already in set return False.
- **3x3 box trick:** make a 3x3 arr of hashsets, box id = `(r//3, c//3)` (// not %), then do the same logic as above.
- **TC:** O(9*9) = O(1) | **SC:** O(1) -> fixed 9x9 board

---

## 8. Encode and Decode Strings (271)
- **Pattern:** Length-prefix encoding
- **LeetCode:** https://leetcode.com/problems/encode-and-decode-strings/
- **Neetcode:** https://neetcode.io/solutions/encode-and-decode-strings
- **Idea:** Can't use a random delimiter (it might exist inside a string). So encode each string as `length + # + string`. While decoding, read digits till `#`, that tells you how many chars to grab next. Even if `#` is inside a string it doesn't matter, we jump by length.
- **TC:** O(n) | **SC:** O(n)

---

## 9. Longest Consecutive Sequence (128)
- **Pattern:** Hash Set (find sequence start)
- **LeetCode:** https://leetcode.com/problems/longest-consecutive-sequence/
- **Neetcode:** https://neetcode.io/solutions/longest-consecutive-sequence
- **Idea:** Dump nums into a set for O(1) lookup. A num is the START of a sequence only if `num-1` is NOT in the set. From a start, keep walking `num+1` and count length. Skip nums in the middle of a seq -> that keeps it O(n).
- **TC:** O(n) | **SC:** O(n)

---

## 10. Maximum Subarray (53)
- **Pattern:** Kadane's Algorithm (running sum)
- **LeetCode:** https://leetcode.com/problems/maximum-subarray/
- **Neetcode:** https://neetcode.io/solutions/maximum-subarray
- **Idea:** Brute force = check all subarrays O(n^2). Kadane: at each i, `curr_sum = max(num, curr_sum + num)` -> if the running sum drags you down, drop it and start fresh from current num. Track the max along the way. Feels like a sliding window.
- **TC:** O(n) | **SC:** O(1)

---

## 11. Subarray Sum Equals K (560)
- **Pattern:** Prefix Sum + Hash Map (two sum combo)
- **LeetCode:** https://leetcode.com/problems/subarray-sum-equals-k/
- **Neetcode:** https://neetcode.io/solutions/subarray-sum-equals-k
- **Idea:** Tricky one. Running prefix sum + two sum on the prefixes. For current sum, a subarray ending here equals k if some earlier prefix = `sum - k`. Keep a hashMap of prefix sum counts and add `prefix[sum-k]` to the answer. Init `prefix[0] = 1` to handle when the whole prefix itself equals k.
- **TC:** O(n) | **SC:** O(n)

---

## TLDR - which pattern when?
- **"seen before / duplicate / pair"** -> Hash Set / Hash Table
- **"anagram / group by letters"** -> freq count as key (tuple)
- **"top k / k most frequent"** -> Bucket Sort (count = index)
- **"product / range without division"** -> Prefix & Postfix
- **"subarray sum / count subarrays"** -> Prefix Sum + Hash Map
- **"longest consecutive run"** -> Set + find the start
- **"max subarray sum"** -> Kadane's
- **grid duplicates** -> Hash Set with `(r//3, c//3)` box id

## Coding tricks (from my notes)
- While loop with no clear exit -> put the `if` condn INSIDE the while as the break -> code gets easy.
- List lookup is O(n), set lookup is O(1) -> convert to set when you need fast access.
- dict keys can't be a list -> use a `tuple`.
- `Counter(iterable)` -> instant freq map shortcut.
