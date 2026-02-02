# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# My way is to find the path from root to the target nodes and then find the common node
# from the to paths stored in the list, I used hashmap to track the LCA
# I am iterating the paths in reverse order to find the LCA
# Use examples and think about this approach
class Solution:
    def print_all_paths(self, root, targetNode, stack, paths):
        if not root:
            return
        
        stack.append(root)

        if root == targetNode:
            paths.append(stack.copy())
        
        self.print_all_paths(root.left, targetNode, stack, paths)
        self.print_all_paths(root.right, targetNode, stack, paths)
        stack.pop()
    
    def lowestCommonAncestor(self, root, p, q):
        stack = []
        paths = []
        self.print_all_paths(root, p, stack, paths)
        # for path in paths[0]:
        #     print(path.val)
          
        self.print_all_paths(root, q, stack, paths)

        # for path in paths[1]:
        #     print(path.val)

        hashMap = {}
        for i in range(len(paths[0])-1,-1,-1):
            if paths[0][i] in hashMap:
                hashMap[paths[0][i]] += 1
            else:
                hashMap[paths[0][i]] = 1

        for i in range(len(paths[1])-1,-1,-1):
            if paths[1][i] in hashMap:
                hashMap[paths[1][i]] += 1
                if hashMap[paths[1][i]] == 2:
                    print(paths[1][i].val)
                    return paths[1][i]
            else:
                hashMap[paths[1][i]] = 1

# Optimal appoarch
# we look for a split here, because if p and q are in different sub trees then the split node is the LCA
# if the p and q are smaller than root.val, then go left subtree
# if the p and q are larger than root.val, then go right subtree
# but the instant the split occurs(they are in different subtress) -> just return that node and 
# carry it atop the recursion to the top/end(recursion) or just return it(iterative)

# Recursion
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        if root.val > p.val and root.val > q.val:
            root = self.lowestCommonAncestor(root.left,p,q)
        elif root.val < p.val and root.val < q.val:
            root = self.lowestCommonAncestor(root.right,p,q)
        return root # split occurs here

# Iterative way - same problem [it's easier than recursion] -> easy to understand       
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root

if __name__ == "__main__":
    # Creating a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)

    # Creating an instance of Solution and calling binaryTreePaths
    sol = Solution()
    print(sol.lowestCommonAncestor(root, root.right, root.left.right))