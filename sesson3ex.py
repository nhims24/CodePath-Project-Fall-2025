#dictionaries --> key value pairs

#leetcode anagram 

#understanding:
#given a list of strings words, group the strings that are anagrams of each other
# ex: "eat" and "tea"

#Ask:
#Can the word list be empty? YES
#Can the word list be one word? YES
#Whats the max?


#Edge case: 
# Empty list
# a list that have one word  

#Generate Test Cases
# x = None -> []
# x = [] -> []
# x = ['cat'] -> [['cat']]
# x = [['cat',''dog']] -> [['cat',''dog']]
# x = ["eat", "tea","tan", "ate", "nat", "bat"] -> 

#Plan
#1. check if the words is null or empty --> return []
#2. initializing empty dictionary 
#3. Loop through each word in the list
    #4. sort the letters alphabetically as a key for the dictionaries table
    #5. if the key doesn't exist in the dict, insert an empty list
    #6. Append the word to the list
#7. extract the values from the dict --> list, and return list 

def group_anagrams(word):
    if not word:
        return []
    
    anagrams = {}

    for i in word:
        key = ''.join(sorted(i)) ##using it to connect the list together into one big string

        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(i)
    
    return list(anagrams.values())
    
#test code
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))