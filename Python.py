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


# To get the data type of a variable, you can use the type() function:
my_var_1 = 'Hello world'
my_var_2 = 21

print(type(my_var_1))  # <class 'str'>
print(type(my_var_2))  # <class 'int'>


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

alphabet = 'abcdefghijklmnopqrstuvwxyz'
shift = 5
shifted_alphabet = alphabet[shift:] + alphabet[:shift]
print(shifted_alphabet)
# Explanation:
# - `alphabet` is the lowercase English alphabet as a string.
# - `shift` is the rotation amount (5).
# - `shifted_alphabet` uses string slicing to rotate the alphabet:
#   take everything from index `shift` to the end, then append the start up to `shift`.
#   This implements a simple Caesar-style rotation.
# - `print` outputs the resulting rotated alphabet (for shift=5 the result is 'fghijklmnopqrstuvwxyzabcde').
# ...existing code...


def caesar():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'


shift = 5
shifted_alphabet = alphabet[shift:] + alphabet[:shift]
translation_table = str.maketrans(alphabet, shifted_alphabet)
text = 'hello world'
encrypted_text = text.translate(translation_table)
print(encrypted_text)


def caesar(text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(
        alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    if shift < 1 or shift > 25:
        return "Shift must be an integer between 1 and 25."

    if not text or shift == 0:
        print(text)
    else:
        encrypted_text = text.translate(translation_table)



full_dot = '●'
empty_dot = '○'
def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return "The character name should be a string"
    if name == "":
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if name == " ":
        return "The character name should not contain spaces"
    stats = [strength, intelligence, charisma]
    if not all(isinstance(stat, int) for stat in stats):
        return "All stats should be integers"
    if not all(stat >= 1 for stat in stats):
        return "All stats should be no less than 1."
    if not all(stat <= 4 for stat in stats):
        return "All stats should be no more than 4."
    if sum(stats) != 7:
        return "The character should start with 7 points."
        message  = """
This is how you can write characters
on multiple lines
"""
course = "Python for Beginners"
print(len(course))  # Output: 20


first_name = "Kamiye"
middle_name = "Oladipo"
last_name = "Ojedokun"
full_name = f"{len(first_name)} {last_name}"
print(full_name)  # Output: Kamiye Ojedokun