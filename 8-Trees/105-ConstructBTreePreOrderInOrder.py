# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# [MED-HARD PROBLEM]
# First just observe both the traversals
# you will notice that in inorder traversal, root is in the middle and left sub tree is in the left of the root
# and right sub tree is in right of the root
# Using that root index, you can also seperate the preorder traversal into right and left sub trees
# now, you just need to the find the root(preorder[0]) and find preorder[0] index in inorder array, based on this divide the problem
# root.left = f(preorder[1:](leave root),inorder[left tree before root])
# root.right = f(preorder[index+1:],inorder[right tree after root]) and return root in the end
# if any of the arrays are empty, just return

# Use this example to think - 
# 3
# 9 20
# 12(right child of 9) 5 7
# preorder = [3,9,12,20,5,7]
# inorder = [9,12,3,5,20,7]
# postorder = [12,9,5,7,20,3]
# Use this to think in recursion
# it will build the left sub tree first and return to the root and go for the right sub tree via the above algo
# Use the lists above to think and observe the division - in preorder(index 0 is the root) so leave it
# in postorder (index -1) is the root so, leave it
class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        inorder_index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:inorder_index+1], inorder[:inorder_index])
        root.right = self.buildTree(preorder[inorder_index+1:], inorder[inorder_index+1:])
        return root

# Leetcode - 106
# To contruct the tree from postorder and inorder (Observe both traversals first)
# -> inorder logic stays the same but in postorder, 
# you come from reverse when passing in recursion
# Division of inorder array is the same and for postorder array, last element is the root so, leave it
# and use the inorder_index(middle) to the divide the postorder array
# Use this example to think - 
# 3
# 9 20
# 12(right child of 9) 5 7
# preorder = [3,9,12,20,5,7]
# inorder = [9,12,3,5,20,7]
# postorder = [12,9,5,7,20,3]

class Solution:
    def buildTree(self, inorder, postorder):
        if not postorder or not inorder:
            return None
        root = TreeNode(postorder[-1])
        inorder_index = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:inorder_index], postorder[:inorder_index])
        root.right = self.buildTree(inorder[inorder_index+1:], postorder[inorder_index:-1])
        return root
        
            
        
        
        