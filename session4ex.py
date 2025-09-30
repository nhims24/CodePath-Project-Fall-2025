#make a count for the function 

#understanding

#Test Cases
# items = none --> {}
# items = [] --> {}
# items = [("fruit", 1), ("fruit", 2), ("fruit",3),] --> {("fruit": 3)}
#items = [("fruits", "apple"), ("vegetables", "carrot"), ("fruits", "banana")]
# -->  {"fruits": 2, "vegetables": 1}

def count_by_category(items):
    if not items:
        return {}
    
    counts = {}

    for item in items:
        k = item[0]

        #if k is not in the counts dictionary 
        #counts [k] = 0

        #counts[k] +=1
    return counts
