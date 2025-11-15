#understanding 
# if the beginning of each word have the same --> common prefix
#flower, flow, flight --> fl
# dog, cat, tree --> no common prefix
# dog --> dog
# [] --> []

#plan
# create an empty string as result 
# loop through it len of the first word
# store the first one as the target
# loop through the rest of the words
# 




#problem 1 
# is_nested 

#Test Cases:
#if string = empty --> return False 
#if string = () --> return True 
# if odd = return false ?
# if even = return true ?

# RECURSION: (())
# if the length is even --> to make sure the parenthesis are paired ?
def is_nested(s):
    #base case
    if s == None:
        return False
    if len(s)%2 != 0:
        return False
    if s == "":
        return True 
    
    right_index = -1
    left_index = -1
    lst = list(s)
    for i in range(0,len(lst)):
        if lst[i] == '(':
            left_index = i
        elif lst[i] == ')':
            right_index = i
        if left_index != -1 and right_index != -1:
            break
    
    if left_index == -1 or right_index == -1:
        return False
    lst.pop(right_index)
    lst.pop(left_index)
    
    return is_nested(''.join(lst))

print(is_nested("((()))")) #True

#problem 2
def count_ones(lst):
	low = 0
	high = len(lst)-1
	first_index = -1
 
	while low <= high:
		mid = low + (high - low) // 2
		if lst[mid] == 1:
			first_index = mid
			high = mid - 1
            # return high - low + 1
		if lst[mid] == 0:
			low = mid + 1
	if first_index == -1:
		return 0
	return len(lst) - first_index

my_list = [0, 0, 0, 0, 1, 1, 1]
print(count_ones(my_list))


   