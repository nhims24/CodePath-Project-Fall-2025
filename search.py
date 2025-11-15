class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#search for the tree nodes 
def search(root, target): #depth first search? 
    if root is None or root.val == target:
        return root #base case?
    elif target < root.val:
        return search(root.left, target)
    else:
        return search(root.right, target)




root = TreeNode(50)
root.left = TreeNode(30)
root.left.left = TreeNode(20)
root.left.right = TreeNode(40)

root.right = TreeNode(70)
root.right.left = TreeNode(60)
root.right.right = TreeNode(80)

target = 41
found_node = search(root,target)
if found_node:
    print(f"Target {target} found in the tree")
else:
    print(f"Target {target} not found int he tree")