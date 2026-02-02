# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# [IMP] Always with bool questions, return f(root.left) and/or f(root.left) -> Easier to propagate False/True Up with this way
# AND -> only one needs to be false for all to be false
# OR -> only one needs to be true for all to be true

# One way is to write the preorder for both the trees and compare
class Solution:
    def preOrder(self, root, preOrder):
        if not root:
            preOrder.append(None)
            return
        preOrder.append(root.val)
        self.preOrder(root.left, preOrder)
        self.preOrder(root.right, preOrder)

    def isSameTree(self, p, q):
        preOrder_p=[]
        preOrder_q=[]

        self.preOrder(p, preOrder_p)
        self.preOrder(q, preOrder_q)

        if preOrder_p == preOrder_q:
            return True
        return False
    
# Other way is to recursively travel both the trees and 
# check if the nodes are same Visualize recursion with two trees
class Solution:
    def isSameTree(self, p, q):
        if not p and not q: # If both p and q are null, tree is same
            return True
        if not p or not q: # if one node is null, false
            return False
        if p.val != q.val: # value is different, false
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) # actual operation happens here

# Other Attempt
class Solution:
    def isSameTree(self, p, q) -> bool:
        if not p and not q:
            return True
        elif p and not q:
            return False
        elif not p and q:
            return False
        elif p and q and p.val!=q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        