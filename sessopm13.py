class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val # <- here
        self.left = left
        self.right = right
#PROBLEM 1
node_one = TreeNode(10) #the root
node_two = TreeNode(4) #left child
node_three = TreeNode(6) # right child

node_one.left = node_two #left side
node_one.right = node_three # right side

#PROBLEM 2 
def check_tree(root): # it has to be root.value?
    # if root.val == root.left.val + root.right.val:
    #     return True
    # return False 
    return root.val == root.left.val + root.right.val

#PROBLEM 3
def check_tree(root):
    # if root.left.val and not root.right.val: 
    #     return root.left.val + 0 == root.val
    # if root.right.val and not root.left.val:
    #     return root.right.val + 0 == root.val
    
    # return root.right.val + root.left.val == root.val
    left_val = root.left.val if root.left else 0
    right_val = root.right.val if root.right else 0
    return left_val + right_val == root.val

print(check_tree(node_one))

#PROBLEM 4
def left_most(root):
	#edge cases:
    #if root = null --> left = None
    #if no left node --> return root.val

    if not root:
        return None
    
    #loop through the binary tree with pointer because linkedlist use pointer
    curr = root
    while curr.left:
        curr = curr.left
    return curr.val

def inorder_traversal(root):
	pass


def remove_node(root, value):
    # Write your code here
    if not root:
        return None
    
    if value < root.val:
        root.left = remove_node(root.left, value)
    elif value > root.val:
        root.right = remove_node(root.right, value)
    else:
        if not root.right:
            return root.left
        elif not root.left:
            return root.right
        
        successor = root.right
        while(successor.left): #check if the left most exist 
            successor = successor.left 
        root.val = successor.val
        
        root.right = remove_node(root.right, successor.val) #delete the sucessor value
    