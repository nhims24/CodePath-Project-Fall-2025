class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# if root is null: return False
# Base Case: 
# Recursive Case:
def is_symmetric(root):
    if not root:
        return False
    if not root.right and not root.left:
        return True
    
    q = []
    
    q.append(root)
    currentLevel = 0
    
    while q:
        len_q = len(q)
        levelList = []

        for i in range(len_q):
            node = q.pop(0) 
            levelList.append(node)
            
            if node.left: 
                q.append(node.left)
            if node.right:
                q.append(node.right)
        currentLevel += 1 
        
        reverseList = levelList.reverse()
        if reverseList != levelList:
            return False
    return True  
# Example Tree #1:

#        1
#      /   \
#     /     \
#    2       2
#   / \     / \
#  3   4   4   3
           

# Example Tree #1
tree = TreeNode(
    1,
    left=TreeNode(
        2,
        left=TreeNode(3),
        right=TreeNode(4)
    ),
    right=TreeNode(
        2,
        left=TreeNode(4),
        right=TreeNode(3)
    )
) 
print(is_symmetric(tree))



#BREADTH FIRST SEARCH IDK HOW TO DO IT CORRECTLY BUT IK IT IS BREADTH FIRST SEARCH
#BECAUSE YOU WILL CHECK THE
#HelloM LEVEL BY LEVEL WHICH IS HOW BREATHFIRST SEARCH WORK LIKE A CHRISTMAS TREE!
#!!!!!!!!
#you want to use queue?? 
#ima just type the code i had and i guess you guys can work it out from there?
# q = deque() --> make the queue to read each level
#q.append(root) --> you add the root first and keep adding through transversal
# while q: --> while q exist 
    #current = [] --> you keep track of the current level you have
    #for i in range(len(q)) --> you will loops through <-I can see this
        
