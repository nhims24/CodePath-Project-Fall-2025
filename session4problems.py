#understand:
# we will need to do use dictionaries access

#plan:
# only check if the candidate in the votes then update the vote
#else the new candidate vote will equal to 1

#problem 1
def cast_vote(votes, candidate):
    #if not votes or candidate:
    #    return []
    
    if candidate in votes:
        votes[candidate] += 1
    else:
        votes[candidate] = 1
    return votes

# votes = {"Alice": 5, "Bob": 3}
# cast_vote(votes, "Alice")
# print(votes)
# cast_vote(votes, "Gina")
# print(votes)

#problem 2

#understand: 
#find the common keys
#there would two list

#plan
#find the common keys 
#loop through the dictionaries to find the similar key
#store the key in the list
#return the list 

#edge case 
#what if the dictionaries is empty ? return {}
#what if the dictionaries is none? return {}
#what if there is no similarities? return {}


def common_keys(dict1, dict2):
   # if not dict1 or dict2:
    #    return [] 
    
    result = []
    for key in dict1:
        if key in dict2:
            result.append(key)
    return result

# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"b": 4, "c": 5, "d": 6}
# common_list = common_keys(dict1, dict2)
# print(common_list)

#problem 3
def count_occurrences(nums):
    key = {}

    for i in nums:
        if(i in nums):
            nums[i] += 1
        
#problem 7
#understand 
#length of list divide two to make the amount of pairs 
#the element of the pair needs to be equal (2,2)

def divide_list(nums):
    pair_value = {}

    for i in nums: #looping through the list to get the key for the dictionary 
        if i in pair_value:
            pair_value[i] += 1
        else:
            pair_value[i] = 1 
    
    for n in pair_value.values(): #check the value of the dictionary 
        if n % 2 == 0:
            return True
    return False 

nums = [3,2,3,2,2,2]
print(divide_list(nums))
nums = [1,2,3,4]
print(divide_list(nums))


def frequency_greater_than_n(nums, n):
    # Write your code here
    key = {}
    
    for i in nums:
        if i in key:
            key[i] += 1
        else:
            key[i] = 1
    
    result = {}
    for k,v in key.items():
        if v > n:
            result[k] = v
    
    return result

nums = [1,1,2,3,3,3,4]
result = {"1": 2, "3": 3}
    

def do_now(nums, target):
    key = {}

    for i in nums:
        if i in key:
            key[i] += 1
        else:
            key[i] = 1
    
    result = {}
    for k,v in key.items():
        for k2,v2 in key.items():
            if k != k2 and k + k2== target:
                result[v] = k
    
    return result

