# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# My appoarch was to traverse every node and check it's root.left.val and root.right.val
# but here I am only comparing small subtrees seperately, a node in a top will violate the codn of node in bottom
# So, we actually need a n2 appoarch here [THINK]
# wrong appoarch
# class Solution:
#     def isValidBST(self, root):
#         if not root:
#             return True
#         if root.left and root.left.val > root.val:
#             return False
#         if root.right and root.right.val < root.val:
#             return False
#         return self.isValidBST(root.left) and self.isValidBST(root.right)

# Optimal appoarch - every node in a BST has a max value and min value, 
# bw that, it can take any value. so, we can change the data structure to include min,max for every node
# OR we can pass them as arguments in recursion OR we can use BFS, queue -> add [node, max, min] for every node

# Main logic here is that when we go left, new node max value = root.val and when we go right, new node min value becomes
# root.val. Tranversing the tree fully, you can assign min and max values for every node

# Using Recursion
class Solution:
    def validBST(self, root, min, max):
        if not root:
            return True
        if root.val >= max or root.val <= min:
            return False
        return self.validBST(root.left, min, root.val) and self.validBST(root.right, root.val, max)
        
    def isValidBST(self, root):
        return self.validBST(root, float('-inf'), float('inf'))

# Using BFS
from collections import deque
class Solution:
    def isValidBST(self, root):
        q = deque()
        q.append([root, float('-inf'), float('inf')]) # 0-node,1-min,2-max (indexes)
        while q:
            node = q.popleft()
            if node[0].val <= node[1] or node[0].val >= node[2]:
                return False
            if node[0].left:
                q.append([node[0].left, node[1], node[0].val])
            if node[0].right:
                q.append([node[0].right, node[0].val, node[2]])
        return True
            
        

        


            