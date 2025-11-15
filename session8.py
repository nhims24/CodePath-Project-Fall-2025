#two pointer problem

#Given a string s, determine if it can become a palindrome by removing at most one character.
#A palindrome is a word, phrase, or sequence that reads the same backward as forward.


#understand
#can the string be null?
#can the string be empty?
#can the string already have palindrome?

#test cases

#s = None -> True
#s = "" -> True
#s = "a" -> True
#s = "abca" -> True
#s = "abc" -> False
#s = "aba" -> True
#s = "abcba" -> True

#match 


def valid_palindrome(s):
    pass


#
# Complete the 'find_min_sublist_sum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER k
#


#understand
#need to implement 2 pointer 
#the edge cases will be if k == 0 --> return 0
#


def find_min_sublist_sum(nums, k):
    # Write your code here

    n = len(nums)
    if n < k or k == 0:
        return 0
    
    left = 0
    right = 0
    
    current_sum = 0
    while right < k:
        current_sum += nums[right]
        right += 1
    
    min_sum = current_sum
    
    while right < n:
        current_sum -= nums[left]
        left+=1
        
        current_sum += nums[right]
        right += 1
        
        if current_sum < min_sum:
            min_sum = current_sum
    
    return min_sum

if __name__ == '__main__':
    nums = [2, 3, 1, 4, 5]
    k = 3
    result = find_min_sublist_sum(nums, k)
    print(result)


#
# Complete the 'find_pair_sum' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER target
#

#understand
#use two pointer to start from the beginning and the end and loop throught it at the same time

def find_pair_sum(s, target):
    # Write your code here

    nums_str = [int(i) for i in str(s)]

    left = 0
    right = 1

    while right < len(nums_str):
        if nums_str[left] + nums_str[right] == target:
            return True
        left += 1
        right += 1
    
    return False
            

if __name__ == '__main__': 
    s = "123456"
    target = 10
    result = find_pair_sum(s, target)
    print(result)