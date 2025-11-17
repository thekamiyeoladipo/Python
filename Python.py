print("Kamiye is learning Python.")

# The most common data types in Python are:
# 1. Integer example
x = 5   
print("Integer:", x, type(x))
# 2. Float example
y = 3.14
print("Float:", y)
# 3. String example 
name = "Kamiye"
print("String:", name)
# 4. Boolean example
is_learning = True
print("Boolean:", is_learning) 
# 5. List example
fruits = ["apple", "banana", "cherry"]
print("List:", fruits)
# 6. Tuple example  
coordinates = (10.0, 20.0)
print("Tuple:", coordinates)
# 7. Dictionary example
person = {"name": "Kamiye", "age": 25}
print("Dictionary:", person)
# 8. Set example
unique_numbers = {1, 2, 3, 4, 5}    
print("Set:", unique_numbers)
# 9. NoneType example
nothing = None  
print("NoneType:", nothing)
# 10. Complex example
complex_number = 2 + 3j
print("Complex:", complex_number)
# These data types are fundamental in Python programming and are used to store and manipulate data in various ways.



#To get the data type of a variable, you can use the type() function:
my_var_1 = 'Hello world'
my_var_2 = 21

print(type(my_var_1)) # <class 'str'>
print(type (my_var_2)) # <class 'int'>



my_str_1 = "Hello"
my_str_2 = 'Kamiye'
str_plus_str = my_str_1 + " " + my_str_2
print(str_plus_str)  # Output: Hello Kamiye




my_int_1 = 10
my_int_2 = 5

sum_ints = my_int_1 + my_int_2
print('Sum of Integers:', sum_ints)  # Output: Sum of Integers 15



name = input('What is your name?')
print('Hello', name)


def hello():
    print("Hello, world!")  
hello()  # Call the function to execute its code


def calculate_sum(a, b):
    return a + b
my_sum = calculate_sum(10, 10)
print(my_sum)  # Output: 20



def my_func():
    my_var = 10
    print(my_var)
my_func()  # Output: 10


age = 18
if age >= 18:
    print("You are a senior man, cheeeee.")
else:
    print("You are a minor.")
