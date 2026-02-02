# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# n time and n space for list
class Solution:
    # Use Preorder
    def DFS(self, root, list, count):
        if not root:
            return
        list.append(root.val)
        if root.val == max(list):
            count[0]+=1
        self.DFS(root.left, list, count)
        self.DFS(root.right, list, count)
        list.pop()
        
    def goodNodes(self, root):
        list = []
        count = []
        count.append(0)
        self.DFS(root, list, count)
        return count[0]


# Instead of using a list, we can use a max value argument for every node and compare 
# if thats greater or lesser to find the good node

# Instead of using res to return answer here you can also use count=[0] as an argument in fn call
class Solution:
    # Use Preorder
    def DFS(self, root, max_value):
        if not root:
            return 0
        res=0 # we can initailize it here because we need the dfs() call to be 0 or 1 only, Actual storage happensin res+=dfs() step[THINK]
        if root.val >= max_value:
            res += 1
        else:
            res += 0
        max_value = max(max_value, root.val)
        res += self.DFS(root.left, max_value)
        res += self.DFS(root.right, max_value)
        return res
      
        
    def goodNodes(self, root):
        return self.DFS(root, float('-inf'))
      


