# Do/See 129 after this [SAME LOGIC]
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def print_all_paths(self, root, stack=[], paths=[]):
        if not root:
            return
        
        stack.append(str(root.val))

        if not root.left and not root.right:
            paths.append("->".join(stack))
        
        self.print_all_paths(root.left, stack, paths)
        self.print_all_paths(root.right, stack, paths)
        stack.pop()
    
    def binaryTreePaths(self, root):
        list = []
        paths = []
        self.print_all_paths(root,list,paths)
        return paths

if __name__ == "__main__":
    # Creating a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)

    # Creating an instance of Solution and calling binaryTreePaths
    sol = Solution()
    print(sol.binaryTreePaths(root))


  

        