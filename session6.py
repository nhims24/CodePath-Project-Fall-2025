
#problem 1
# We need ot convert to integer (cast)
# return sum of integers

#Edge cases
# null or empty retrun -> -1
# nums = ["10"] --> 10

#pseudocode 
#func sum_of_number_string(nums)
#   if nums is empty -
        #return -1
#   total_sum = 0
#   for every i in nums:
#       total_sum += int(i)
#   return total sum


def sum_of_number_strings(nums):
    if not nums:
        return -1
    total_sum = 0
    for i in nums:
        total_sum += int(i)
    return total_sum

nums = []
#nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
#print(sum)

#problem 2
#set() doesn't take any duplicates

#plan
#1. make a new list 
#2. loop throught the values check if its duplicate, append to new_list if not
#3. return new_list

#pseudocode
# func remove_duplicates(nums):
# no_dup = []
# i = 0
# while.(i < len(nums)).:
# if num[i] is not in no_dup:
#   append num[i] to no_dup
# return no_dup

#Pseudo code improved
#set automatically remove dup

# func remove_duplicates(nums):
# make a new set 
# append the value from the list to the set 
# convert set back to list
# return the list 

#code
def remove_duplicates(nums):
    mySet = set()
    mySet.update(nums)
    newList = list(mySet)
    return newList

nums = [1,1,1,2,3,4,4,5,6,6]
print(remove_duplicates(nums))

#Ayinde Abrams do you wanna team up with both of us?

#problem 3
#plan 
#create a new string(?)
#using 2 pointer?
#isalpha()
s="python"
reversed_s = s[::-1]
result = reversed_s + "rocks!"
print(result)

date = "DD-02-YYYY"
month = date[3:5]
valid = int(month) >=1 and int(month)<=12
print(valid)
