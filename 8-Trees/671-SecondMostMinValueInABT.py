# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root) -> int:
        second_min_val = float('inf')
        min_val = root.val
        def dfs(root):
            nonlocal second_min_val
            if not root:
                return
            if root.val > min_val:
                second_min_val = min(root.val, second_min_val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        if second_min_val == float('inf'):
            return -1
        return second_min_val