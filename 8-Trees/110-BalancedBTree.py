# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# [FOLLOW UP TO THE MAX DEPTH PF THE BTREE QUESTION]
# From the question, realize that we need to find leftDepth - rightDepth
# we also need the height of the BT in recursion, so, use a helper fn, maxDiff argument and 
# find the maxDifference depth for every node

# [TIP] We can use a argument in helper fn as an array to get the value after fn call without 
# returning the value
class Solution:
    def leftRightDiff(self, root, max_diff):
        if not root:
            return 0
        leftDepth = self.leftRightDiff(root.left, max_diff)
        rightDepth = self.leftRightDiff(root.right, max_diff)

        diff = abs(leftDepth - rightDepth)
        if max_diff[0] < diff:
            max_diff[0] = diff

        return 1 + max(leftDepth, rightDepth)
    
    def isBalanced(self, root):
        max_diff = []
        max_diff.append(0)
        self.leftRightDiff(root, max_diff)
        if max_diff[0] > 1:
            return False
        return True
