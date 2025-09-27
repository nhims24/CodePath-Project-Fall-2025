#problem 2
#def doubled(lst):
#    if not lst:
#        print([])
 #   for i in lst:
#        print(i*2)
#
#lst=[1,2,3]
#doubled(lst)

#problem 3
def doubled2(lst):
    if not lst:
        print([])
    
    new_list = [] #you telling the computer than the result must be a list 
    for i in lst:
        new_list.append(i*2) 
    print(new_list)

lst = [1,2,3,4]
doubled2(lst)

#problem 4
def flip_sign(lst):
    if not lst:
        print([])
    
    flipped_list = [] #you telling the computer than the result must be a list 
    for i in lst:
        flipped_list.append(i*-1) 
    print (flipped_list)

lst = [1,2,3,4]
flip_sign(lst)