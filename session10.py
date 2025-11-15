#In Class problem
# give a string s, find the first on-repeating char
# if not exist --> -1
# e.g. s = "leetcode" --> return 0
# s = "loveleetcode" --> return 2
# s = "aabb" --> return -1

#def first_non_repeating_char(s):
     


#Problem 1

#Understanding
# loop through the linked list
    # if tail point to the next head node
        #return true
    # else
        #return false 

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()
        
# return False if head is None
# curr = head
# while curr
    # in this loop, increment curr
    # if curr is equal to head, then return true
# return false 
'''def is_circular(head):
    if not head:
        return False
	
    curr = head
    while curr:
        curr = curr.next
        if curr == head:
            return True
    return False 


head = Node(1)
node1 = Node(2)
node2 = Node(3)
node3 = Node(4)

head.next = node1
node1.next = node2
node2.next = node3

print(is_circular(head))'''

# num1 -> num2 -> num3 -> num4 -> num2
#          ⬆︎  - - - - - - -|

# if head is null, return None
# make slowPt and fastPt
# find out if there's a cycle in the first place
    # while loop 
        # go through all the logic for this loop
# after we get initial position
# slow -> num4
# fast -> num4
# slow pointer to the head -> num1
# leave the fast pointer to initial position -> num3
# while loop
    # in this while loop, we will traverse the slow pointer and fast pointer one node ahead
    #iteration 1
    # fast.next and slow.next are the same 
    # return fast

def find_last_node_in_cycle(head):
    if not head:
        return None
    
    slowPt = head
    fastPt = head
    
    #Find out if we have a cycle
    while fastPt.next and fastPt.next.next: 
        slowPt = slowPt.next
        fastPt = fastPt.next.next #<---- right here it should be fastPT.next.next
        
        if slowPt == fastPt:
            break #cycle detected and both fast and slow are at the same node 
    
    else: 
        return None
    
    slowPt = head
    #Maybe fro this one while loop could be like while slowPt != fastPtr? imnot sure tho <- ahhhhhhhh <- this could work
    while slowPt != fastPt:  # still not wokring for this while loop
        slowPt = slowPt.next
        fastPt = fastPt.next
    return fastPt
    # test this real quick
    #Imma ask chat ok so IT says: for line 88 there is a problem casue we didnt move the pointer fast
    
head = Node(1)
node1 = Node(2)
node2 = Node(3)
node3 = Node(4)

head.next = node1
node1.next = node2
node2.next = node3
node3.next = node1

print(find_last_node_in_cycle(head))

class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

def find_nth_from_end(head, n):
    # Write your code here
    if head is None:
        return None
    
    curr = head
    length = 0
    while curr:
        length+=1
        curr = curr.next
        
    if n > length:
        return None
    
    curr = head
    for i in range (length - n):
        curr = curr.next 
    
    return curr.value   

def shuffle(head):
    # Write your code here
    # if not head or not head.next:
    #     return head

    # # new head should be the second node (since we swap first pair)
    # new_head = head.next

    # prev = None
    # current = head

    # # loop through pairs
    # while current and current.next:
    #     first = current
    #     second = current.next
    #     next_pair = second.next  # store next pair’s first node

    #     # swap the pair
    #     second.next = first
    #     first.next = next_pair

    #     # connect previous pair’s tail to this swapped pair
    #     if prev:
    #         prev.next = second

    #     # move forward
    #     prev = first
    #     current = next_pair

    # return new_head
    
    curr = head
    while curr and curr.next:
        curr.value, curr.next.value = curr.next.value, curr.value # a = b
        curr = curr.next.next
    return curr 

class Node:
   def __init__(self, value, next_node = None):
       self.value = value
       self.next = next_node

def find_intersection(head_a, head_b):
    # Write your code here
    if not head_a and not head_b:
        return None
    
    first = head_a
    second = head_b
    
    while first is not second:
        first = first.next if first else head_b
        second = second.next if second else head_a
    return first