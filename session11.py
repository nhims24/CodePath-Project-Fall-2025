''' Problem 1
def repeat_hello(n):
	if n > 0:
		print("Hello")
		repeat_hello(n - 1)
repeat_hello(5)

def repeat_hello_iterative(n):
	for i in range(0, n):
		print("Hello")

print("Recursive Function: ")
repeat_hello(5)

print("Iterative Function: ")
repeat_hello_iterative(5)'''


''' Problem 2
# Base Case:  n <= 1
# Recursive Case: !5 = 5 * 4 * 3 * 2 * 1 --> n*(n-1)
def factorial(n):
	if n <= 1: 
		return 1
	return n * factorial(n-1) # factorial function for recursion

print(factorial(5))'''

#Problem 3
# if its empty --> return 0
# Recursive Case: Split the list from after the first element to the end
def sum_list(lst):
	if not lst: # base case 
		return 0
	if len(lst) == 1: #base case 
		return lst[0]# Example Input: [1, 2, 3, 4, 5]
	return lst[0] + sum_list(lst[1:])
		
# Example Input: [1, 2, 3, 4, 5]
lst = [1, 2, 3, 4, 5]
print(sum_list(lst))

#Problem 5
def binary_search(lst, target):
	pass
	# Initialize a left pointer to the 0th index in the list
	# Initialize a right pointer to the last index in the list
	
	# While left pointer is less than right pointer:
		# Find the middle index of the array
		
		# If the value at the middle index is the target value:
			# Return the middle index
		# Else if the value at the middle index is less than our target value:
			# Update pointer(s) to only search right half of the list in next loop iteration
		# Else
			# Update pointer(s) to only search left half of the list in next loop iteration
	
	# If we search whole list and haven't found target value, return -1
	# [1, 2, 3, 4, 5]
	
def binary_search(lst, target):
	left = 0
	right = len(lst) - 1

	while left <= right: 
		mid = left + (right - left) // 2 #getting an integer
		if lst[mid]== target:
			return mid
		elif lst[mid] < target: 
			left = mid + 1 #right half
		else:
			right = mid - 1	 #left half 
			
		
