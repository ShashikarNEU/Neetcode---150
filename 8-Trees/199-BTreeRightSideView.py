# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root):
        queue = deque()
        levelOrder = []
        currentOrder = []
        if not root:
            return levelOrder
        queue.append(root)
        queue.append(None)
        while queue:
            node = queue.popleft()
            if not node:
                if queue:
                    queue.append(None)
                levelOrder.append(currentOrder)
                currentOrder = []
            else:
                currentOrder.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return levelOrder
          
    def rightSideView(self, root):
        levelOrder = self.levelOrder(root)
        rightSideView= []
        for level in levelOrder:
            rightSideView.append(level[-1])
        return rightSideView
    
    def leftSideView(self, root):
        levelOrder = self.levelOrder(root)
        rightSideView= []
        for level in levelOrder:
            rightSideView.append(level[0])
        return rightSideView
    
    # leetcode 513 - return the leftmost bottom value(last level) of the BTree
    def findBottomLeftValue(self, root):
        levelOrder = self.levelOrder(root)
        return levelOrder[-1][0]