from collections import deque

# For printing binary tree in level order, we use BFS
# so, we need a queue - enqueue root, None at first
# dequeue from the queue and check left child and right child -> 
# add them to the queue. while dequeing if not none, print it. if none, insert another null
# so that, you can break the line for a new level

# [IMP] -> when encountering null, we push a other null only if the queue is not empty. if it's empty
# it will cause a infinite loop[THINK]
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        queue = deque()
        levelOrder = []
        currentOrder = []
        if not root:
            return levelOrder
        queue.append(root)
        queue.append(None)
        while queue:
            node = queue.popleft()
            if not node:
                if queue:
                    queue.append(None)
                levelOrder.append(currentOrder)
                currentOrder=[]
                #print("\n")
                continue # you can use continue or else here
            #print(node.val, end=" ")
            currentOrder.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return levelOrder

# Helper function to build a tree from a list (for easy testing)
def build_tree(nodes):
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1

    while i < len(nodes):
        current = queue.popleft()
        if nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1

        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1

    return root

# Example usage
if __name__ == "__main__":
    # Example: [3,9,20,None,None,15,7] -> Output: [[3],[9,20],[15,7]]
    tree_nodes = [3, 9, 20, None, None, 15, 7]
    root = build_tree(tree_nodes)
    s = Solution()

    print("Level Order Traversal:", s.levelOrder(root))
            




        