"""Here are all the solutions to the exercises and Challenges"""

"""===================== Module 1 ==========================="""

"""
    =========== Exercise 1 =============
    Using a list, create a shopping list of 5 items. Then
    print the whole list, and then each item individually.
"""

shopping_list = [] # Fill in with some values

user_input = input("Enter Item: ")
shopping_list.append(user_input)

user_input = input("Enter Item: ")
shopping_list.append(user_input)

user_input = input("Enter Item: ")
shopping_list.append(user_input)

user_input = input("Enter Item: ")
shopping_list.append(user_input)

user_input = input("Enter Item: ")
shopping_list.append(user_input)

print(shopping_list) # Print the whole list

print(shopping_list[0]) # Print item 1

print(shopping_list[1]) # Print item 2

print(shopping_list[2]) # Print item 3

print(shopping_list[3]) # Print item 4

print(shopping_list[4]) # Print item 5



"""
    =========== Exercise 2 =============
    Find something that you can eat that has nutrition
    facts on the label. Fill in the dictionary below with
    the info on the label and try printing specific information.
    If you can't find anything nearby you can use this example: https://www.donhummertrucking.com/media/cms/Nutrition_Facts_388AE27A88B67.png
"""
# When ready to work on these exercises uncomment below code

nutrition_facts = {
    "Total Fat":"8g",
    "Cholesterol":"0mg",
    "Sodium":"5mg",
    "Total Carbohydrate":"22g",
    "Protein":"2g"} # Fill in with the nutrition facts from the label

print(nutrition_facts) # Print all the nutrition facts

print(nutrition_facts["Sodium"]) # Prints out sodium content; in this case 5mg

"""
    =========== Exercise 3 =============
    Python has a function built in to allow you to
    take input from the command line and store it.
    The function is called input() and it takes one
    argument, which is the string to display when
    asking the user for input.
    Here is an example:
    ```
    >> name = input('What is your name?: ')
    >> print(name)
    ```
    Using the information about type casting take an input
    from the command line (which is always a string), convert
    it to an int and then double it and print it.
    i.e. if the user provides 21 then the program should print 42
"""

# When ready to work on these exercises uncomment below code

age = input('What is your age?: ')

print(int(age) * 2) # Find a way to convert the age to an int and multiply by 2

"""
    =========== Challenge 1 =============
    Under the hood in python strings are actually
    collections that use indices. 
    Knowing this figure out how to print the fourth 
    letter of the string below.
"""

name = "John Doe"

print(name[3]) # Since 3 is the index of the 4th element you can print it directly

"""
    =========== Challenge 2 =============
    Create an empty list called shopping_list
    then using user input fill the list with 5
    elements.
    Hint: You can do this with 6 variables including the list
"""
# When ready to work on these exercises uncomment below code

shopping_list = [] # Create a variable called shopping list with nothing in it

# Add 5 items to the shopping list

user_input = input("Enter Item: ")
shopping_list.append(user_input)
user_input = input("Enter Item: ")
shopping_list.append(user_input)
user_input = input("Enter Item: ")
shopping_list.append(user_input)
user_input = input("Enter Item: ")
shopping_list.append(user_input)
user_input = input("Enter Item: ")
shopping_list.append(user_input)

print(shopping_list) # print out the final list


"""===================== Module 2 ==========================="""

"""
    =========== Exercise 1 =============
    I have provided some starter code below
    that creates a result variable, and a number_1
    variable. Your goal is to make number_1 equal 11
    after the operations that have been done to it.
"""

result = 0
number_1 = 5
number_1 += 52

# Do more operations on number 1 until it equals eleven

# There are a ton of ways to do this here is one:

number_1 //= 3 # number_1 == 19
number_1 -= 8 # number_1 == 11


result = number_1
print(result == 11)


"""
    =========== Exercise 2 =============
    Take input from the command line, and convert it to
    an int. Now pick a range (i.e. 0-10), and create a set
    of conditional statements that prints the string
    representation of the number input by the user.
    For example if someone put in 8, then it would print 'eight'.

    Hint: Use if, elif and else statements.
"""

user_choice = int(input("Enter a number between 0-10:"))

if user_choice == 0:
    print("Zero")

elif user_choice == 1:
    print("One")

elif user_choice == 2:
    print("Two")

elif user_choice == 3:
    print("Three")

elif user_choice == 4:
    print("Four")

elif user_choice == 5:
    print("Five")

elif user_choice == 6:
    print("Six")

elif user_choice == 7:
    print("Seven")

elif user_choice == 8:
    print("Eight")

elif user_choice == 9:
    print("Nine")

elif user_choice == 10:
    print("Ten")

else:
    print("Number is out of range")

"""
    =========== Exercise 3 =============
    Before running the code below try to
    figure out which print statement will
    execute and why. Then uncomment the code
    and check if you were right.
"""

# number = 0
# number += 15
# number //= 2
# number *= 6
# number -= 4

# if number < 10:
#     print("Less than 10")

# elif 10 <= number <= 20:
#     print("Between 10 and 20")

# elif 20 <= number <= 30:
#     print("Between 20 and 30")

# elif 30 <= number <= 40:
#     print("Between 30 and 40")

# else:
#     print("¯\_(ツ)_/¯")

"""Here is the explanation number starts as 0
then it is 'plus-equalled' to 15 it's then 
'integer-divide-equalled' to 2 making it 7
then 'multiply-equalled' to 6 making it 42,
then finally 'minus-equalled' to 4 making it 38.

Because the number is now 38 the program will print:
    'Between 30 and 40'
"""

"""============== Challenges ================"""

"""
    =========== Challenge 1 =============
    Take an input from the command line, then
    convert it to an int and if it is even 
    print 'the number is even' otherwise print
    'the number is odd'.
"""

number = int(input("Please enter a number: "))

if number % 2 == 0:
    print("Number is Even")

else:
    print("Number is Odd")

"""
    =========== Challenge 2 =============
    Take an input from the command line, and 
    convert it to an int. Validate the number
    is within the range 1-5, and then for each
    possible value (1-5), write the code to make
    the input 11.
    I.e. Someone inputs 1 the result is 11, if someone
    inputs 2 the result is 11 etc. If someone puts in a
    number not in range (1-5) print:
        'value not between 1-5 please try again'

    Hint: You should have between 6-7 if/elif/else statements
"""



number = int(input("Please enter a number between 1-5: "))

# These answers are not the only possible answers

if number == 1:
    number += 10 # 1 + 10 is eleven

elif number == 2:
    number *= 5 # 2 * 5 is 10
    number += 1 # 10 + 1 is 11

elif number == 3:
    number *= 4 # 3 * 4 is 12
    number -= 1 # 12 - 1 is 11

elif number == 4:
    number *= 3 # 4 * 3 is 12
    number -= 1 # 12 - 1 is 11

elif number == 5:
    number += 6 # 5 + 6 is 11 

else:
    print("Number is not in range 1-5")


"""
    =========== Challenge 3 =============
    There are functions in python that can be used
    to determine if strings contain certain characters.

    For example the function isdigit() returns True if
    ALL the characters in the string are digits. Here
    is an example of it's usage:

        numbers = "1234567"
        letters = "Hello 4"

        print(numbers.isdigit()) # prints True
        print(letters.isdigit()) # prints False

     There are two other similar functions called endswith()
     and islower(). 

     endswith() takes a string as an argument
     and returns true if the string it's being used on ends with
     the string provided.

     islower() returns true if the string provided is all lowercase

     Now take input at the command line, and using if statements print
     the following statements if conditions are met:
        1. if the string is all numbers print "All numbers"
        2. If the string is all lowercase print "All lowercase"
        3. If the string ends with "yes" print "Ends in yes"
        Otherwise print "None of the conditions have been met"
"""

user_input = input("Please enter some text: ")

if user_input.isdigit():
    print("All Numbers")

elif user_input.islower():
    print("All lowercase")

elif user_input.endswith("yes"):
    print("Ends in yes")

else:
    print("None of the conditions have been met")


"""===================== Module 3 ==========================="""

"""
    =========== Exercise 1 =============
    Take the current for loop below and add
    two conditions to the loop body:
        1. If 'Eggs' are the current element, then conitnue
        2. If 'Sausages' is the current element, stop iterating.
"""

shopping_list = ["Bread", "Bannanas", "Pineapples", "Eggs", "Oranges", "Milk", "Sausages"]

for item in shopping_list: # Iterate over the items in the shopping list
    if "Eggs" in item:
        continue
    elif "Sausages" in item:
        break
    else: 
        print(item)

"""
    =========== Exercise 2 =============
    Take the current existing shopping list
    and ask the user to add a number of items
    to the list.
    For example, if someone enters 3 then prompt
    them for input and append it to the list 3 times.
"""

shopping_list = []

amount_to_add = int(input("How many items do you want to add?"))

counter = 0 # A counter to keep track of the number of items that have been added

while counter < amount_to_add:
    item = (input("What item would you like to add?: "))
    shopping_list.append(item)
    counter += 1

print(shopping_list)

"""
    =========== Challenge 1 =============
    The code below generates a random number
    make a game that loops and takes user input 
    at the command line. The input is the user's
    guess at what the number is. Taking their input
    you should print either: 'too high', 'too low' or
    'Correct guess'.
    For example let's assume the number is 4 a sample
    output of the game would look like this:
        >> Enter Guess: 2
        Too Low
        >> Enter Guess: 5
        Too High
        >> Enter Guess: 4
        Correct Guess
"""

import random

number = random.randint(0, 10) # Generates a random number

correct_guess = False

while not correct_guess:
    guess = int(input("What is your guess?: "))

    if guess < number:
        print("Too Low")
    
    elif guess > number:
        print("Too High")

    elif guess == number:
        print("Correct Guess")
        correct_guess = True


"""
    =========== Challenge 2 =============

    Take two inputs from the command line, then
    convert both to an int the first number will
    be the starting number, and the second will be
    the ending number. Create a loop that goes from
    the starting number to the ending number, and only
    prints the even numbers.
"""

start = int(input("Starting number: "))
end = int(input("Ending number: "))

x = start # Initialize x to the starting value

while x <= end:
    if x % 2 == 0: # If the current x value is even
        print(x)
        x += 1 # Increment x by 1

    else:
        x += 1 # Increment x by 1



"""
    =========== Challenge 3 =============

    THIS CHALLENGE IS HARD, DON'T GET DISCOURADGED
                IF YOU CAN'T DO IT!

    Using the list below print the numbers
    in ascending order. It should look like this: 
    1
    2
    3
    4
    5
    6
    7
    8
    9

    HINT: The simplest (and shortest) way to do this
    is with a loop counter variable, and a while loop.
"""

# This one is pretty hard, in the video for this lesson I explain it in depth.

numbers = [
    [1,4,7],
    [2,5,8],
    [3,6,9]
]

x = 0 # Used to count how many itterations to do
while x < 3: # Loop while x is less than the number of sublists in numbers
    print(numbers[0][x]) # Take the first lists x'th term and print it
    print(numbers[1][x]) # Take the Second lists x'th term and print it
    print(numbers[2][x]) # Take the Third lists x'th term and print it
    x += 1 # Increment loop counter by 1

"""===================== Module 4 ==========================="""

"""
    =========== Exercise 1 =============

    Add a docstring to the function below.
    The function takes a list and prints all 
    the items in the list.

    Bonus: Try using type declaration for the argument.
"""

def print_list(list_to_parse: list):
    """Takes in a list and print's it's items
    
    Parameters
    ----------
    list_to_parse:
        The list you want to print the items of."""
    for item in list_to_parse:
        print(item)

"""
    =========== Exercise 2 =============

    Implement the delete_item() function
    below, all the details to do so should
    be there for you.

    Hint: you can use del(list[index]) to remove
    an item from a list.
"""

def delete_item(list_to_parse, item_index):
    """Takes a list, removes an item at the 
    specified index and returns the list
    
    Parameters
    ----------
    list_to_parse:
        The list to remove the item from
    
    item_index:
        The index to remove an item from
    
    Returns
    -------
    The list with the item removed
    """
    del(list_to_parse[item_index]) # Remove the item
    return list_to_parse

shopping_list = ["eggs", "ham", "sausages"] # A test list to remove an item from

shopping_list = delete_item(shopping_list, 1) # Should remove 'ham' from the list

print(shopping_list)

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
    """ Takes a string and validates it against
    three criteria:
        1. The input is all lowercase (use variable.islower())
        2. It doesn't end with 'yeet'
        3. There are no q's in the input.
    
    Parameters
    ----------
    user_input:
        The value to validate.
    
    Returns
    -------
    True if none of the criteria are met and False
    if any are.
    """

    if not user_input.islower():
        return False

    if user_input.endswith("yeet"):
        return False
    
    if "q" or "Q" in user_input: # Check if q is a letter
        return False
    
    return True # If none of the conditions above are met

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
    """
    Adds a value to a dictionary with a given key
    
    Parameters
    ----------
    dictionary:
        The dictionary to add the key-value pair to.
    
    key:
        The key to be added for the value to be added.
    
    Value:
        The value to be added for the key to be added.

    Returns
    -------
    The dictionary with the key-value added.
    """
    dictionary[key] = value
    return dictionary

def print_dictionary(dictionary: dict):
    """
    Prints the keys and values of a dictionary.
    
    Parameters
    ----------
    dictionary:
        The dictionary to print.
    """
    for key in dictionary:
        print(key, dictionary[key])

user = {
    "name": "Kieran Wood",
    "age" : 21
}

user = add_to_dictionary(user, "country", "Canada")

print_dictionary(user)


"""===================== Module 5 ==========================="""

import datetime # SEE: https://docs.python.org/3/library/datetime.html and the extras module for details

"""
    =========== Exercise 1 =============
    Write the estimate_planks function so that it returns the correct
    number of planks (use integer division to avoid complication).

    Example:


"""
class Contractor:
    def __init__(self, plank_length = 1):
        """A Demo class representing a construction Contractor.
        
        Attributes
        ----------
        plank_length(int): The length of wooden planks in feet; Default: 1
        
        Methods
        -------
        estimate_planks: Estimates the amount of planks needed to build a structure based on provided length.
        """
        self.plank_length = plank_length
    
    def estimate_planks(self, length):
        """Estimates the amount of planks needed to build the structure, based on the length

        Parameters
        ----------
        length(int): How long the structure that needs to be built is.

        """
        number_of_planks = length // self.plank_length
        return f"You need {number_of_planks} plank(s) of wood to build this wall"

dave = Contractor(2)
print(dave.estimate_planks(10)) # Should be 5 planks

billy = Contractor(5)
print(billy.estimate_planks(225)) # Should be 45 planks

"""
    =========== Exercise 2 =============
    Write a user class that has 3 attributes and 1 method:
        Attributes:
            1. name(str): users full name
            2. birthday(datetime.date): Users birthday as a datetime object
            3. premium (boolean): True or false based on if user is a premium user or not
        Method:
            1. next_birthday: A method that returns a string of the users birthday this year, if it is today then return 'Happy Birthday!' instead.
    
"""
class User:
    def __init__(self, name, birthday, premium):
        """A Demo class representing a user for an application.
        
        Attributes
        ----------
        name: (str)
            The users' name.

        birthday: (datetime.date)
            The date of birth for the user.

        premium: (bool)
            Represents whether a user is a premium user or not.

        
        Methods
        -------
        next_birthday: 
            Determines the users' birthday in the current year and prints it.
        """
        self.name = name
        self.birthday = birthday
        self.premium = premium

    def next_birthday(self):
        """Determines the users' birthday in the current year and prints it"""
        if self.birthday == datetime.date.today():
            print("Happy Birthday!")

        else:
            current_year = datetime.date.today().year
            birth_month = self.birthday.month
            birth_day = self.birthday.day
            print(datetime.date(current_year, birth_month, birth_day))
        
john = User("John Doe", datetime.date(1995,10,25), True)
print(john.next_birthday()) # You will have to validate this yourself
print("John Doe" in john.name)  # Should print True
print(john.premium) # Should Print True


"""
    =========== Exercise 3 =============
    Take the previous user class from before, and add a class docstring to it.
"""

# I already did the above exercise, take a look at exercise 2 for answer