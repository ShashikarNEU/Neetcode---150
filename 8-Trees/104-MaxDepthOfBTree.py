# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# To understand this code, look at the recursion from the last
# since all logic is written after the traversal, it will go to the end and return 0
# while coming back, for leaf node (leftDepth,rightDepth are 0) so, maxDepth will be 1
# so, from the smallest sub tree, we are looking at the height and add 1 as it goes up 
# the tree seperately for right sub tree and left sub tree

#Long code to understand better
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        maxDepth = max(leftDepth, rightDepth)
        return 1 + maxDepth
    
# Short Code
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))