num1 = 42 #variable declaration, primitive, numbers
num2 = 2.3 #variable declaration, primitive, numbers
boolean = True # variable declaration, primitive, boolean
string = 'Hello World' # variable declaration, primitive, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, data types, composite, list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, data types, composite, dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, data types, composite, tuples
print(type(fruit)) #log statement;
print(pizza_toppings[1])#log statement;
pizza_toppings.append('Mushrooms')#tuples, #add value;
print(person['name'])#log statement;
person['name'] = 'George'#dictionary, change value;
person['eye_color'] = 'blue'#dictionary, add value;
print(fruit[2])#log statement;

if num1 > 45: #conditional, if
    print("It's greater") #log statement;
else: #conditional, else
    print("It's lower")#log statement

if len(string) < 5: #conditional, if
    print("It's a short word!")
elif len(string) > 15:#conditional, else if
    print("It's a long word!") #log statement
else: #conditional, else
    print("Just right!") #log statement

for x in range(5): #
    print(x) #log statement 
for x in range(2,5):
    print(x) #log statement
for x in range(2,10,3):
    print(x) #log statement
x = 0
while(x < 5): #while loop, stop
    print(x) #log statement
    x += 1 # while loop, increment

pizza_toppings.pop() #list, delete value
pizza_toppings.pop(1) #list, delete value

print(person) #log statement
person.pop('eye_color') #dictionary, delete value
print(person) #log statement

for topping in pizza_toppings: #for loop, list
    if topping == 'Pepperoni': #conditional, if
        continue #for loop, continues the loop
    print('After 1st if statement') #log statement
    if topping == 'Olives': #conditional, if
        break# for loop, end the loop

def print_hello_ten_times(): #function
    for num in range(10): #for loop, in range 0-9
        print('Hello')# log statement

print_hello_ten_times() #log statement

def print_hello_x_times(x): #function, parameter
    for num in range(x): #for loop, parameter
        print('Hello') # log statement

print_hello_x_times(4)#log statement

def print_hello_x_or_ten_times(x = 10): #function, argument
    for num in range(x): #for loop, parameter
        print('Hello') #log statement

print_hello_x_or_ten_times() #log statement
print_hello_x_or_ten_times(4) #log statement, argument


"""
Bonus section
"""

# print(num3) 
# num3 = 72
# fruit[0] = 'cranberry' #NameError: name <variable name> is not defined
# print(person['favorite_team']) #KeyError: 'favorite_team'
# print(pizza_toppings[7]) IndexError: list index out of range
#   print(boolean)
# fruit.append('raspberry') # AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) # AttributeError: 'tuple' object has no attribute 'pop'