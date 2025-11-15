class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
    
    def bark(self):
        return "Woof!"
    
dog1 = Dog("Buddy", "Golden Retriever", "Alice")
dog2 = Dog("Max", "Beagle", "Bob")

print(dog1.bark())
print(dog2.bark())

#
# Complete the 'extend_linked_list' function below.
#
# The function is not expected to return anything.
# The function accepts following parameters:
#  1. STRING tail
#  2. LIST(STRING) values
#

# list = a -> b -> c
#curr = tail 
#for value in values:
    #new_node = Node(value)
    #current.next = new_node
    #curr = curr.next 

class Node: 
    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

def extend_linked_list(tail, values):
    # Write your code here
    curr = tail
    for value in values:
        new_node = Node(value)
        curr.next = new_node
        curr = curr.next

class Node: 
    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

def copy_first_n_nodes(head, n):
    # Write your code here
    if not head: #edge cases 
        return None
    
    curr = head
    count = 0
    new_head = None
    tail = None
    
    while curr and count < n:
        new_node = Node(curr.value)
        if new_head is None:
            new_head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = tail.next
        curr = curr.next
        count+=1
    
    return new_head