# [FOLLOW UP TO MAX DEPTH OF A BT QUESTION - 104]
# Here the logic is same as depth of a Binary tree
# you need to add left sub tree depth and right sub tree depth
# but if you return 1+leftDepth+rightDepth, unwanted depth gets considered[THINK], 
# we need only height of left tree and right tree for every node and add them to 
# find the max. so, use a helper fn with diameter(max of leftdepth+rightDepth) as an argument

# [TIP] We can use a argument in helper fn as an array to get the value after fn call without 
# returning the value
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterBT(self, root, diameter):
        if not root:
            return 0
        leftDepth = self.diameterBT(root.left, diameter)
        rightDepth = self.diameterBT(root.right, diameter)
        depthSum = leftDepth + rightDepth
        diameter[0] = max(depthSum, diameter[0])
        return 1 + max(leftDepth, rightDepth)
        
    def diameterOfBinaryTree(self, root):
        diameter = [0]
        self.diameterBT(root,diameter)
        return diameter[0]

# Other Attempt
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        maxDiameter = 0
        def longestDiameter(root):
            nonlocal maxDiameter
            if not root:
                return 0

            leftH = longestDiameter(root.left)
            rightH = longestDiameter(root.right)

            maxDiameter = max(maxDiameter, leftH+rightH)

            return 1+max(leftH, rightH)
        
        longestDiameter(root)
        return maxDiameter

if __name__ == "__main__":
    # Example Tree: [1,2,3,4,5]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    sol = Solution()
    print(sol.diameterOfBinaryTree(root))  # Expected output: 3