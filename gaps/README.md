# Gap Coverage Checklist (by pattern)

Missing from this repo, grouped by pattern with difficulty. Ranked within each
group by 2026 frequency (Amazon, Google, LinkedIn).

Targets: Amazon SDE1/SDE2, Google L3/L4, LinkedIn equivalent.

---

## Sliding Window
- [ ] 76 Minimum Window Substring | HARD | top-25 across 40 companies, Amazon top-100, Google hard tester | https://leetcode.com/problems/minimum-window-substring/
- [ ] 438 Find All Anagrams in a String | MEDIUM | completes the window set | https://leetcode.com/problems/find-all-anagrams-in-a-string/

## Cyclic Sort
- [ ] 41 First Missing Positive | HARD | named core pattern in 2026 Amazon/Google/Meta writeups | https://leetcode.com/problems/first-missing-positive/
- [ ] 448 Find All Numbers Disappeared in an Array | EASY | https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
- [ ] 268 Missing Number | EASY | doubles as bit (XOR) warmup | https://leetcode.com/problems/missing-number/

## Two Heaps
- [ ] 295 Find Median from Data Stream | HARD | standard heap-section classic, missing from your Heap folder | https://leetcode.com/problems/find-median-from-data-stream/

## Design
- [ ] 460 LFU Cache | HARD | Amazon top-100, harder sibling of LRU (#1 overall) | https://leetcode.com/problems/lfu-cache/
- [ ] 380 Insert Delete GetRandom O(1) | MEDIUM | active at LinkedIn (Staff, hard variant), Bloomberg, Docusign | https://leetcode.com/problems/insert-delete-getrandom-o1/
- [ ] 716 Max Stack | HARD | LinkedIn staple | https://leetcode.com/problems/max-stack/

## Trie
- [ ] 211 Design Add and Search Words Data Structure | MEDIUM | completes your 208/212 | https://leetcode.com/problems/design-add-and-search-words-data-structure/

## Bit Manipulation (warmups only, rest skippable)
- [ ] 136 Single Number | EASY | XOR trick | https://leetcode.com/problems/single-number/
- [ ] 191 Number of 1 Bits | EASY | https://leetcode.com/problems/number-of-1-bits/
- [ ] 338 Counting Bits | EASY | DP + bits | https://leetcode.com/problems/counting-bits/

## Intervals
- [ ] 1851 Minimum Interval to Include Each Query | HARD | Google L4 tail, skip otherwise | https://leetcode.com/problems/minimum-interval-to-include-each-query/

## Segment Tree / BIT (Google L4 only)
- [ ] 315 Count of Smaller Numbers After Self | HARD | https://leetcode.com/problems/count-of-smaller-numbers-after-self/
- [ ] 307 Range Sum Query Mutable | MEDIUM | https://leetcode.com/problems/range-sum-query-mutable/

---

## Difficulty count
HARD 7 (76, 41, 295, 460, 716, 1851, 315) | MEDIUM 4 (438, 380, 211, 307) | EASY 5 (448, 268, 136, 191, 338)

## Notes
- Bit manipulation is in none of the 2026 company frequency lists. The 3 easies
  are enough; skip the rest for these targets.
- The 7 hards overlap heavily with "clear all NeetCode hards." Doing that knocks
  out 76, 41, 295, 460 in one pass. The non-hard gaps (380, 716 design, 211,
  438, plus cyclic-sort easies) are the ones you'd otherwise miss.
- Remaining work after this is hard-problem volume under time pressure, not new
  topics.
