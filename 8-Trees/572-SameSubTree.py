# [FOLLOW UP TO SAME BTREE QUESTION - 100]
# Idea here is to tranverse the root tree and have the isSameTree fn run for every root node and root of the subroot node
# we can decrease the usage of isSameTree by running this fn only if root.val == subroot.val. without helper fn, have the nesscary
# TRUE AND FALSE conditions and return f(root.left) or f(root.right). since it's or, getting one true means that that True will
# be given to the top of recursion safely.(no need to use argument, subTree[0])

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# With use of a helper fn
class Solution:
    def isSameTree(self, p, q):
        if not p and not q: # If both p and q are null, tree is same
            return True
        if not p or not q: # if one node is null, false
            return False
        if p.val != q.val: # value is different, false
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) # actual operation happens here
    
    def helperFn(self, root, subRoot, subTree):
        if not root:
            return
        
        if root.val == subRoot.val and not subTree[0]:
            subTree[0] = self.isSameTree(root, subRoot)

        self.helperFn(root.left, subRoot, subTree)
        self.helperFn(root.right, subRoot, subTree)
    
    def isSubtree(self, root, subRoot):
        subTree = []
        subTree.append(False)
        self.helperFn(root, subRoot, subTree)
        return subTree[0]

# Without use of helper fn 
def isSubtree(self, root, subRoot):
    if not root:
        return False
    if self.isSameTree(root, subRoot):
        return True
    return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

def main():
    # Example Test Case
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)

    subRoot = TreeNode(4)
    subRoot.left = TreeNode(1)
    subRoot.right = TreeNode(2)

    sol = Solution()
    result = sol.isSubtree(root, subRoot)
    print("Is subRoot a subtree of root?", result)

if __name__ == "__main__":
    main()
        