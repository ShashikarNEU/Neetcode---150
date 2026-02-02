# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self, root, list):
        if not root:
            return
        self.inOrder(root.left, list)
        list.append(root.val)
        self.inOrder(root.right, list)

    def kthSmallest(self, root, k):
        list = []
        self.inOrder(root, list)
        return list[k-1]