# Example 2: Enumerate with start value specified
#cereals = ['cheerios', 'fruity pebbles', 'cocoa puffs']
#for count, cereal in enumerate(cereals, start=1):
 # print(count, cereal)


#problemex
#A pangram is a sentence that contains every letter of 
# the English alphabet at least once, regardless of case. 
# Write a function to determine if a given sentence is a pangram.

#Input: sentence = "The quick brown fox jumps over the lazy dog"
#Output: True

#Test Cases
#sentence = None --> False
#sentence = '' --> False
#sentence = '1' --> False
#sentence = 'a' --> False
#sentence = 'abcdefghijklmnopqrstuvwxyz' --> True
#sentence = 'abcdefghijklmno*pqrstuvwxyz' --> True
#sentence = 'The quick brown fox jumps over the lazy dog' --> True

## Psecuedo 
#func is_panagram(sentence)
#  if sentence is null or empty:
#       return false

#  initilaize an empty set called letters
#  len of eng_alphebtically = 26

#  for every char in sentence 
#       if char is alphabetical
#           add to the letters set the lowercased version of char 
#   return len of letters set is equivalent to 26 

ENGL_ALPHABET_SIZE = 26

def is_pangram(sentence):
    if not sentence:
        return False
    
    letters = set() #declare an empty set 
    
    for char in sentence:
        if char.isalpha():
            letters.add(char.lower())


    return len(letters) == ENGL_ALPHABET_SIZE

#print(is_pangram('1'))
#print(is_pangram('The quick brown fox jumps over the lazy dog'))

#problem 1
def count_mississippi(limit):
    for num in range(1, limit+1):
        print( f"{num} mississippi")

#count_mississippi(5)



#problem 2

#Plan
#    check if the string is empty or not --> ''
#    convert the string into a list of character 
#    swap the last index to the first index 
#    first index = 0 and last index = -1 
#    use join method to convert back as a string 

#Psuedocode 
#func swap_ends(my_str):
    #if my_str is empty or null:
        #   return []
    #list_of_char = list(my_str)
    #swap(list_of_char[0], list_of_char[len(list_of_char)-1])
    #return ''.join(list_of_char)

def swap_ends(my_str):
    if not my_str:
        return ""
    list_of_char = my_str[-1]+my_str[1:-1]+my_str[0] #string concatenation
    return list_of_char

#print(swap_ends("hello"))   

#problem 3
ENGL_ALPHABET_SIZE = 26

def is_pangram(sentence):
    if not sentence:
        return False
    
    letters = set() #declare an empty set 
    
    for char in sentence:
        if char.isalpha():
            letters.add(char.lower())


    return len(letters) == ENGL_ALPHABET_SIZE
#problem 4

# Write a function reverse_string() that takes a
# string my_str as a parameter and returns the string reversed.
def reverse_string(my_str):
    result = my_str[::-1] #reverse in string first (:) = beginning, second(:) = last, # = order
    return result

#print(reverse_string("hello nyc"))

#problem 5
def first_unique_char(my_str):
    count = 0
    for i in my_str:
        pass
    