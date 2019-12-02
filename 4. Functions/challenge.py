"""
    =========== Challenge 1 =============

    create a function called validate_input(),
    that takes a string, and returns True if the 
    following conditions are met, and False if they
    aren't:
        1. The input is all lowercase (use variable.islower())
        2. It doesn't end with 'yeet'
        3. There are no q's in the input.
    
    Hint: if you use a for loop you can see each letter of a
    string, or the in operator to check for a value in a string.
"""

user_input = "this is valid"
user_input_1 = "This has a capital"
user_input_2 = "this has a yeet"
user_input_3 = "this has a q"

def validate_input(user_input: str) -> bool:
    """TODO: Docstring, and function logic"""
    pass # Remove this after implementing the function

print(validate_input(user_input)) # Should be True
print(validate_input(user_input_1)) # Should be False
print(validate_input(user_input_2)) # Should be False
print(validate_input(user_input_3)) # Should be False

"""
    =========== Challenge 2 =============

    Create two functions (with docstrings):
     1. add_to_dictionary(): that takes a dictionary,
        a key, and a value as arguments, then returns
        the dictionary with the key and value added.
    2. print_dictionary(): A function that takes a 
       dictionary as an argument and prints it's
       keys and values.
    
    Hint: If you loop over a dictionary with a for loop
        each iteration is a key.
    
    Extra Hint: Keys are how you access values in a dictionary.
"""

def add_to_dictionary(dictionary: dict, key: str, value) -> dict:
    """TODO: Docstring, and function logic"""
    # Your code goes here
    return dictionary

def print_dictionary(dictionary: dict):
    """TODO: Docstring, and function logic"""
    # Your code goes here

user = {
    "name": "Kieran Wood",
    "age" : 21
}

user = add_to_dictionary(user, "country", "Canada")

print_dictionary(user)