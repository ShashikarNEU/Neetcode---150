# Definition for a binary tree node.
from typing import Optional

"""
=========================================
📝 IMPLEMENTATION NOTES: House Robber III
=========================================

📌 Concept: Tree DP (State-Tracking)
Instead of returning a single maximum value from your recursive helper, 
return an array/tuple that tracks the maximum money for **every possible state** of the current node. This eliminates the need to look at grandchildren (node.left.left) 
or use a memoization hash map.

The Two States:
Every call to dfs(node) returns: [rob_this_node, skip_this_node]

🧠 The Transition Logic:
1. If you ROB the current node:
   You trigger the alarm for its immediate children. Therefore, you are *forced* to take the "skipped" values from both the left and right children.
   -> current_robbed = node.val + left_skipped + right_skipped

2. If you SKIP the current node:
   The alarm is safe. The children are "unlocked." For *each* child independently, 
   you can choose whichever option (robbed or skipped) yielded the most money.
   -> current_skipped = max(left_robbed, left_skipped) + max(right_robbed, right_skipped)

⏱️ Complexity:
- Time: O(N) — We visit every node exactly once (standard post-order traversal).
- Space: O(H) — Where H is the height of the tree (recursion stack memory). 
                Worst case O(N) for skewed tree, O(log N) for balanced tree.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def houseRobber3(root):
            if not root:
                return 0,0
            
            [max_left_robbed, max_left_skipped] = houseRobber3(root.left)
            [max_right_robbed, max_right_skipped] = houseRobber3(root.right)

            current_robbed = root.val + max_left_skipped + max_right_skipped
            current_skipped = max(max_left_robbed, max_left_skipped) + max(max_right_robbed, max_right_skipped)

            return [current_robbed, current_skipped]
        
        root_robbed, root_skipped =  houseRobber3(root)
        return max(root_robbed, root_skipped)