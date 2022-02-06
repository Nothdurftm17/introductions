#1 Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
def countdown(x):
    output=[]
    for i in range(x,-1,-1):
        output.append(i)
    print(output)
countdown(5)

# Create a function that will receive a list with two numbers. Print the first value and return the second.
def print_and_return(a,b):
    print(a)
    return b

c = print_and_return(1,2)
print(c)

def first_plus_length(x):
    result = x[0] + len(x)
    return result
y=first_plus_length([1,2,3,4,5])
print(y)

def values_greater_than_second(x):
    if len(x) < 2:
        return false
    output = []
    for i in range(0,len(x)):
        if x[i] > x[1]:
            output.append(x[i])
    print(len(output))
    return output 
print(values_greater_than_second([5,2,3,2,1,4]))

#Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.

def length_and_value(size,value):
    newList = []
    for i in range(size):
        newList.append(value)
    return newList
print(length_and_value(4,7))










