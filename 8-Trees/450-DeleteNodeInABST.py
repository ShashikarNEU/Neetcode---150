# Watch video first, https://www.youtube.com/watch?v=LFzAoJJt92M
# First, search for the value using BST property
# then, after you find it
# 3 cases
# case 1 - if right is none, case 2- if left is none and case 3- both are present
# case 1 - return root.left, case 2 - return root.right
# case 3 - find the right subtree's min or left subtree's max, assign it to root.val, then, perform delete recursively

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Equal Case
            # Here, There are 3 cases
            # if right is none, if left is none and both are present
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # Both subtrees are present case
                # Here, you have two options, find the right subtree's min or left subtree's max, assign it to root.val, then, perform delete recursively
                curr = root.right
                while curr.left:
                    curr = curr.left
                
                root.val = curr.val
                # Delete the min val recursively
                root.right = self.deleteNode(root.right, root.val)

        return root