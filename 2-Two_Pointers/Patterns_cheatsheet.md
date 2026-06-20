# Two Pointers - Pattern Revision List

Quick revision before interviews. Read the pattern, recall the trick, move on.
n = input size unless mentioned otherwise.

**Two types of two pointers:**
- **Opposite ends:** p1 at start, p2 at end, converge to middle. Usually on a SORTED arr. Move left/right based on a condn. (sum-pair, range problems)
- **Same direction:** slow + fast pointer. Used in linked lists, cycle detection, sliding window. Exit condn `while fast and fast.next`.

---

## 1. Valid Palindrome (125)
- **Pattern:** Opposite ends pointers
- **LeetCode:** https://leetcode.com/problems/valid-palindrome/
- **Neetcode:** https://neetcode.io/solutions/valid-palindrome
- **Idea:** p1 at start, p2 at end. Compare chars, if mismatch -> not a palindrome. Else move both inward. Keep only alphanumeric chars (`isalnum()`) and compare in `.lower()`.
- **TC:** O(n) | **SC:** O(n) for the cleaned list (O(1) if you skip non-alnum in place)

---

## 2. Two Sum II - Input Array Sorted (167)
- **Pattern:** Opposite ends pointers (sorted two sum)
- **LeetCode:** https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
- **Neetcode:** https://neetcode.io/solutions/two-sum-ii-input-array-is-sorted
- **Idea:** Array is sorted -> p1 at start, p2 at end. `sum = a[p1]+a[p2]`. If sum == target -> answer. If sum > target -> p2-- (need smaller). If sum < target -> p1++ (need bigger). This is THE base pattern for opposite pointers.
- **TC:** O(n) | **SC:** O(1)

---

## 3. Three Sum (15)
- **Pattern:** Sort + fixed i + sorted two sum
- **LeetCode:** https://leetcode.com/problems/3sum/
- **Neetcode:** https://neetcode.io/solutions/3sum
- **Idea:** Brute force is O(n^3), so sorting is "free" (O(nlogn) < n^3). Sort, then for-loop picks `i`, and inside run sorted two sum (start=i+1, end=last) looking for sum == 0.
- **The duplicates trap (recall this!):** dupes only matter when sum == 0 (the case we ADD to result). Two places to skip:
  - outer loop: `if i > 0 and nums[i] == nums[i-1]: continue` (don't redo same work)
  - after adding: skip dupes on start and end before moving both.
  - For sum < 0 / sum > 0 we don't add anything, so dupes don't matter there.
- **TC:** O(n^2) | **SC:** O(1) (ignoring sort + output)

---

## 4. Container With Most Water (11)
- **Pattern:** Opposite ends pointers (move the smaller wall)
- **LeetCode:** https://leetcode.com/problems/container-with-most-water/
- **Neetcode:** https://neetcode.io/solutions/container-with-most-water
- **Idea:** p1 at start, p2 at end. `area = min(height[p1], height[p2]) * window`. Water is capped by the SHORTER wall, so move the smaller pointer inward (hope to find a taller wall). Shrink window each step, track maxArea.
- **TC:** O(n) | **SC:** O(1)

---

## 5. Trapping Rain Water (42)
- **Pattern:** Two pointers with leftMax / rightMax
- **LeetCode:** https://leetcode.com/problems/trapping-rain-water/
- **Neetcode:** https://neetcode.io/solutions/trapping-rain-water
- **Core formula:** water at index i = `min(leftMax_before_i, rightMax_after_i) - height[i]`. (index height itself not counted)
- **Two pointer way:** pointers at both ends + leftMax, rightMax. If `leftMax <= rightMax` move left in (we know left side is the limiting one, so water there = leftMax - height), else move right in. Add water, then update that side's max.
- **3-list way (easier, more space):** build leftMax arr + rightMax arr, then for each i add `min(left[i], right[i]) - height[i]`. SC O(n).
- **TC:** O(n) | **SC:** O(1) two-pointer / O(n) 3-list

---

## 6. Longest Palindromic Substring (5)
- **Pattern:** Expand around center (same-place 2 pointer)
- **LeetCode:** https://leetcode.com/problems/longest-palindromic-substring/
- **Neetcode:** https://neetcode.io/solutions/longest-palindromic-substring
- **Idea:** Brute force = list all substrings + check each -> O(n^3). Optimal O(n^2) = expand around center. For each letter, start left=right=i and expand out while `s[left]==s[right]` -> gives ODD length palindromes. For EVEN, start left=i, right=i+1 and expand the same way. Track the longest.
- **TC:** O(n^2) | **SC:** O(1)

---

## TLDR - which pattern when?
- **sorted arr + find a pair/sum** -> opposite ends pointers
- **3sum / 4sum** -> sort, fix one, run sorted two sum inside (watch dupes)
- **max area / two walls** -> opposite ends, move the smaller one
- **trapping water** -> two pointers w/ leftMax & rightMax (or prefix/suffix max arrs)
- **palindrome substring** -> expand around center (odd + even)
- **linked list / cycle / sliding window** -> slow + fast (same direction)

## Coding tricks (from my notes)
- Opposite pointer base move: `sum > target -> p2--`, `sum < target -> p1++`.
- Skipping dupes only matters where you ADD to the result.
- Same-place expand: do odd (i,i) and even (i,i+1) passes.
- Fast/slow exit: `while fast and fast.next`.
