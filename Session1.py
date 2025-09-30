#problem 1
def hello_world():
    print("Hellow world!")
#hello_world()

#problem 2
def todays_mood():
    mood = ":)"
    print("Today's mood: " + mood)
#todays_mood()

#problem 3
def print_menu(menu):
    print("Lunch today is: " + menu)
#print_menu("pizza")

#problem 4
def sum(a,b):
    return a + b
#print(sum(8,20))

#problem 5
def product(x,y):
    return x * y
#print(product(22,7))

def classify_age(age):
    if age < 18:
        return "child"
    else:
        return "adult"
#print(classify_age(5))

#problem 7
def what_time_is_it(hour):
    if hour == 2:
        return "taco time"
    if hour == 12:
        return "peanut butter jelly time"
    else:
        return "nap time"
#time = what_time_is_it(5)
#print(time)

#problem 8
def blackjack(score):
    if score == 21:
        print("Blackjack!")
    elif score > 21:
        print("Bust!")
    elif score >= 17 and score < 21:
        print("nice hand!")
    else:
        print("hit me!")
#blackjack(19)

#problem 9
def get_first(lst):
    if not lst:
        return None
        
    return lst[0]
#print(get_first([3,1,6,7,5]))

#problem 10
def get_last(list):
    if not list:
        return None
    return list[len(list)-1]
#print(get_last([3,1,6,7,5]))

#problem 11
def counter(stop):
    for i in range(stop):
       print(i)
#counter(7)

#problem 12
def sum_ten():
    num = [1,2,3,4,5,6,7,8,9,10]
    result = 0
    for i in num: #print out 54 first because add up the index instead of the value 
        result += i
    return result 
#print(sum_ten()) 

#problem 13
def sum_positive_range (stop):
    result = 0
    for i in range(stop+1):
        result += i
    return result 
#print(sum_positive_range(6))

#problem 14
def sum_range(start, stop):
    result = 0
    for i in range(start,stop+1):
        result += i
    return result 
#print(sum_range(3,9))

#problem 15
def print_negatives(lst):
    result = []
    if not lst:
        return []
    for i in lst:
        if i < 0:
            result.append(i)
    return result
#print(print_negatives([3,-2,2,1,-5]))