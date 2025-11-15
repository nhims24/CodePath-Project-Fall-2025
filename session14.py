def find_target(lst,target):
    left = 0
    right = lst.length() - 1
    while left <= right:
        mid = (right + left) //2
        if lst[mid] == target:
            return mid
        if lst[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1


class TreeNode():
     def __init__(self, key, value, left=None, right=None):
            self.key = key
            self.val = value
            self.left = left
            self.right = right

#PROBLEM 1    
# A binary tree is uni-valued if every node in the tree has the same value. 
# Given the root of a binary tree, r
# return True if the given tree is uni-valued and False otherwise.
# Evaluate the time complexity of your solution.
# check left and right side?

# edge cases: 
# empty --> return False
# only root --> return true
# two nodes --> Return true if all the same if not retrun False
# go through this recursively, by comparing each value in the tree to each other
# compare the root to the recurse of root.right and root.left 
'''def is_univalued(root):
    if not root:
        return True
    def dfs(node, val): #helper function handle the child node 
        if not node:
            return True
        if node.val != val: #check the child value to its parents value
            return False
        return dfs(node.left, val) and dfs(node.right, val)

    return dfs(root, root.val) #recursive to handle the whole tree to its parents value

    #return root.val == is_univalued(root.left) and root.val == is_univalued(root.right)
    #return dfs(node, val)
    # 1
   #  / \
   # /   \
  # 1     1
 # / \     \
 #1   1     1


#tree 1
root = TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(1)

root.left.left = TreeNode(1)
root.left.right = TreeNode(1)

root.right.right = TreeNode(1)

#tree 2
root1 = TreeNode(1)
root1.left = TreeNode(1)
root1.right = TreeNode(1)

root1.left.left = TreeNode(1)
root1.left.right = TreeNode(2)

root1.right.right = TreeNode(1)

print(is_univalued(root))
print(is_univalued(root1))'''

#Edge cases:
# empty -> -1
# only the root --> return 1
     # 4
 #    / \
 #   /   \
 #  2     5
 # / \    
 #1   3    
# 
# single node -> 0
# recursively search through the right subtree and left subtree 
# for each recursive search, we want to add 1 in our return statement
# we can use the max function, to return the max(rightSubTree, leftsubStree)
#PROBLEM 2
'''def height(root):
    if not root:
        return 0
    if not root.right and not root.left:
        return 1
    
    return 1 + max(height(root.right), height(root.left)) #cumulate the height
    

root = TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(1)

root.left.left = TreeNode(1)
root.left.right = TreeNode(1)

root.right.right = TreeNode(1)

print(height(root))'''

# edge cases:
    # if not root: return false
    
def insert(root, key, value):
	pass