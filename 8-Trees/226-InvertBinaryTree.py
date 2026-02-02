# Definition for a binary tree node.

# Recursively visit each node of the tree with 
# left sub tree and right sub tree then swap the 
# nodes, return root in every step

# For return root, we are returning the recursion root in that recursion step. so, finally whole root will be returned when it exits recursion
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root):
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# Example usage
def print_tree(root):
    if not root:
        return
    print(root.val, end=' ')
    print_tree(root.left)
    print_tree(root.right)

if __name__ == "__main__":
    # Creating a sample binary tree
    tree = TreeNode(4,
                    TreeNode(2, TreeNode(1), TreeNode(3)),
                    TreeNode(7, TreeNode(6), TreeNode(9)))
    
    print("Original Tree:")
    print_tree(tree)
    
    sol = Solution()
    inverted_tree = sol.invertTree(tree)
    
    print("\nInverted Tree:")
    print_tree(inverted_tree)
