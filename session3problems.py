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


lst_1 = [1, 2]
lst_2 = [1, 2, 3]
lst_3 = []
lst_4 = []
print(all_in(lst_3, lst_4))
print(all_in(lst_2, lst_1))
print(all_in(lst_3, lst_2))
print(all_in(lst_1, lst_2))
            
