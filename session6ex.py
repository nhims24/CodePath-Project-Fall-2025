#test cases
#s = "" --> ""
#s = " " --> ""

#Plan
#1. Strip the string
#2. split the string to an array of string
#3. iterate through the array but from back to front, creating a new array 
#4. join the resulting array into a new string
#5. return the new string 

#pseudocode 
# func reverse_words(s):
#     strip_letter = s.strip(" ")
#     splits_str = strip_letter.split()
#     reversed_splits = []
#     for i in range (len(splits_str)-1, splits_str[0]):
#        append word to reversed_splits
#     end

#     reversed_s = join reversed_splits together
#     return reversed_s
# end 

def reverse_words(s):
    stripped_str = s.strip()
    splits_str = stripped_str.split()

    reversed_splits = []

    i = -1
    while abs(i) <= len(splits_str): #could write in different way too (maybe with for loop?)
        reversed_splits.append(splits_str[i])
        i -= 1

    result = " ".join(reversed_splits)
    return result 

#print(reverse_words("s"))