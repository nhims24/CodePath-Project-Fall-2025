#problem 1

#Understand:
#There are two parameters a and b
# every element in list a must be in list b to return true
# list of integer 

#Wonder question
#Will it be more efficient to use dictionaries or list? LIST

#plan
#1. if null or empty --> return []
#2. use nest for loops for list a and b
    #3. if value a = b --> return true 
    #4. if value a != b --> return false 

def all_in(a, b):
    if not a or not b:
        return []
    
    tracker = True 

    for i in a:
        if i in b:
            tracker = True
        else:
            tracker = False
    return tracker


# lst_1 = [1, 2]
# lst_2 = [1, 2, 3]
# lst_3 = []
# lst_4 = []
# print(all_in(lst_3, lst_4))
# print(all_in(lst_2, lst_1))
# print(all_in(lst_3, lst_2))
# print(all_in(lst_1, lst_2))
            
#problem 2
def create_dictionary(keys, values):
    result = {}
    for i in range (len(values)): #loops through the value in the value list
        result[keys[i]] = values[i]

    return result

# keys = ['peanut', 'dragon', 'star', 'pop', 'space']
# values = ['butter', 'fly', 'fish', 'corn', 'ship']
# print(create_dictionary(keys, values))

#problem 3
#understand
# take a dictionary and target 
#check if the dictionary has the target
#then return the keys and its value
#if not return the pair DNE

#example for get() method
# d = {'a': 1, 'b': 2, 'c': 3}
# print(d.get('a'))       # Outputs: 1
# print(d.get('z'))       # Outputs: None
# print(d.get('z', 'Not Found'))  # Outputs: 'Not Found'

def print_pair(dictionary, target):

    if target in dictionary:
        result = dictionary.get(target)
        print("Key:", target)
        print("Value:", result)
    else:
        print("That pair does not exist!")


dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")


#problem 8
#understand
#take in a list return a dictionary
#the dictionary will look like an array or list in python

def index_to_value_map(lst):
    result = {}
    for i in range (len(lst)):
        result[i] = lst[i]
    return result

lst = ["apple", "banana", "cherry"]
print(index_to_value_map(lst))

