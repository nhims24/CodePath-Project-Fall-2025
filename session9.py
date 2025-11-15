#PROBLEM 1
# parameters self and the opponent
# when we call the attack function
# opponent hp is decreased
	# decreased by the damage of self 
	# if the opponents health is less than or equal to 0
	# set the health of the opponent to 0
	# print out the given statement
# print out the other statement


'''class Pokemon():
	def  __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp # hit points
		self.damage = damage # The amount of damage this pokemon does to its opponent every attack
		
	def attack(self, opponent):
		opponent.hp -= self.damage

		if opponent.hp <= 0:
			opponent.hp = 0
			print(opponent.name + " fainted")
		else:
			print(self.name + " dealt " + str(self.damage) + " damage " + opponent.name)

pikachu = Pokemon("Pikachu", 35, 20)
bulbasaur = Pokemon("Bulbasaur", 45, 30) 

opponent = bulbasaur
pikachu.attack(opponent)'''

#PROBLEM 2
'''class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
  
pokemonList = ["Jigglypuff", "Wigglytuff"]

node_1 = Node(pokemonList[0]) #set the value node 1
node_2 = Node(pokemonList[1]) #set the value node 2

node_1.next = node_2

print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next)'''

#PROBLEM 3
'''class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
		
def add_first(head, new_node):
	new_node.next = head
	return new_node'''

#PROBLEM 4
'''class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
  
def get_tail(head):
    if not head:
        return None
    
    curr = head
    
    while curr.next != None:
        curr = curr.next
    return curr.value
              

	
# Build: num1 -> num2 -> num3
num1 = Node("num1")
num2 = Node("num2")
num3 = Node("num3")
num1.next = num2
num2.next = num3

head = num1
tail = get_tail(head)   # or get_tail(num1)
print(tail)             # expected: num3'''


#PROBLEM 5
'''class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
  # 1 -> 2 -> 2 -> 5 -> 4 -> 7 -> 2
  
def ll_replace(head, original, replacement):
	if not head:
		return

	curr = head
	
	while curr:
		if curr.value == original:
			curr.value = replacement	
		curr = curr.next
	return None
	
 
def to_string(head): # to test your list
    parts, cur = [], head
    while cur:
        parts.append(str(cur.value))
        cur = cur.next
    return " -> ".join(parts) if parts else "EMPTY"



num3 = Node(5)
num2 = Node(6, num3)
num1 = Node(5, num2)
# initial linked list: 5 -> 6 -> 5
print(to_string(num1))

head = num1
ll_replace(head, 5, "banana")
print(to_string(head))'''

	#OR YOU CAN TYPE YOUR LINKED LIST HERE IF YOU GUYS WANT ---->
	#here:
	#
	#
	#

class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
    

            
