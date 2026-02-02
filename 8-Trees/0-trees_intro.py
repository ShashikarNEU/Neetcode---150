from collections import deque

# In a BST, value of a node is always larger than all the nodes of it's 
# left sub tree and smaller than all the nodes of its right sub tree
# Refer notes, for n depth there are 2**n-1 nodes in a BST

# Traversals of a BST - 
# preorder(val,left,right) --> we print the value first, go left till null, then, go right if right not visited
# inorder(left,val,right) --> keep on going left, if none print value, then go up, print values, only if the value is printed, go right
# postorder(left,right,val) --> only if both right and left are visited, we print the value

# [IMP] These different trversals explained above are examples of DFS in a Binary Tree. 
# DFS - Depth First Search, we reach the end first, then
# backtrack, look for right child and so on using recursion.

# Applications of the traversals
# Preorder -> Print all paths from root to leaf
# Inorder -> Sorting(Ascending)
# Postorder -> Deleting a node

# Node class representing each node in the BST
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Tree class containing BST operations
class Tree:
    def __init__(self):
        self.root = None

    # Insert a node into the BST
    def insertIntoBST(self, root: "Node", value):
        if root is None:
            return Node(value)
        if value > root.value:
            root.right = self.insertIntoBST(root.right, value)
        else:
            root.left = self.insertIntoBST(root.left, value)
        return root
    
    # Inorder traversal (Left -> Root -> Right)
    # Application -> Sorting
    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.value, end=" ")
        self.inorder(root.right)
    
    # Preorder traversal (Root -> Left -> Right)
    def preorder(self, root):
        if root is None:
            return
        print(root.value, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)
    
    # Postorder traversal (Left -> Right -> Root)
    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.value, end=" ")
    
    # Preorder application: Print all paths from root to leaf
    # Use a stack here, when the node is a leaf, print the stack. 
    # we pop the element when both left and right are visited

    # When we are using a list in argument to record the data, 
    # list bw recursion does not get altered, it is constant
    def print_all_paths(self, root, stack=[]):
        if not root:
            return
        
        stack.append(root.value)

        if not root.left and not root.right:
            print(stack[0:len(stack)])
        
        self.print_all_paths(root.left, stack)
        self.print_all_paths(root.right, stack)
        stack.pop()

    def inorder_append(self,root,list):
        if not root:
            return
        self.inorder_append(root.left,list)
        list.append(root.value)
        self.inorder_append(root.right,list)

    def sort_using_inorder(self, root):
        list = []
        self.inorder_append(root, list)
        return list
    
    def postorder_deleteTree(self, root):
        if not root:
            return
        
        self.postorder_deleteTree(root.left)
        self.postorder_deleteTree(root.right)
        root.left = None
        root.right = None

        
# Call the test function
if __name__ == "__main__":
    values = [6, 2, 7, 1, 4, 9, 3, 5, 8]
    tree = Tree()
    root = None
    for value in values:
        root = tree.insertIntoBST(root, value)
    
    print("\nInorder traversal (sorted order):")
    tree.inorder(root)
    
    print("\nPreorder traversal (root-to-leaf paths):")
    tree.preorder(root)
    
    print("\nPostorder traversal (deleting tree order):")
    tree.postorder(root)

    print("All paths from root to leaf:")
    tree.print_all_paths(root, [])

    print("Sorting using inorder:")
    print(tree.sort_using_inorder(root))

    print("delete using postorder:")
    tree.postorder_deleteTree(root)
    # Delete the first node after this, root = None
    tree.inorder(root)




  