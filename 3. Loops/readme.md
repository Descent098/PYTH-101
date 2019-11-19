# Loops



## Loops



Loops are statements used in python to repeat things *iteratively*. Iterating just means to do something one after another, For example counting from one to 10 requires you to count the current number and then move on the the next *iteration* until you reach 10. 

In practice this means that loops are used to execute code multiple times until a certain condition is met. For example you could *loop* through the numbers 1-10 and print them out one after another.

All loops are composed of the *loop type* (while, for etc.) followed by the *terminating condition* (when the loop should end) and the *loop body* (what the loop should do on each *iteration.*)



### while



A *while* loop is exactly as it sounds, it **loops** will continue **until** the condition is **False**. The basic syntax for a while loop looks like this: 

```python
while condition:
	# Do stuff at this indentation level while condition is True 
# Stuff at this indentation will run after the loop finishes
```



So for example, if you wanted to count from 0-10 and print every number on each loop the code would look like this:

```python
x = 0 # Setup a variable to use for the conditional

while x <= 10: # Continue looping until x is greater than 10
	print(x) # Print the current itterations value of x
	x += 1 # Inrement x by 1 (add 1 to the current value of x)

print("loop Finished") # This will execute after the loop since it's at a lower indentation level
```



### For



For loops are a bit more complicated than while loops. They loop based on *iterables*, which are things in python that you can *iterate over*. Collections such as lists, and tuples (and even strings) are examples of *iterables*.



The basic syntax of a for loop looks like this:



```python
for variable in iterable:
	# Code at this indentation executes during the iteration
# Code at this indentation does stuff after the loop
```



Where variable is an arbitrarily named variable used to hold the current value of the iteration, and iterable is the item to iterate over.



Let's take the example of a shopping list and say you wanted to loop through the values in the list and print them off one by one, you could use a for loop to do this:



```python
shopping_list = ["Eggs", "Ham", "Milk"]

for item in shopping_list: # Iterate through the shopping list
	print(item) # Print the item at the current iteration
```



This would print:



```python
>> Eggs
>> Ham
>> Milk
```



### break



The break statement is used to end a loop immediately. It can (but does not have to) be used with if/elif/else statements to force a loop to stop iterating if a condition is met.



Let's take the example that we want to create a for loop that print's out each letter of a string, but if the string contains a hyphen (-) then we want the loop to end. The code would look like this:

```python
greeting = "Hello-World" # Setting up a string to iterate through

for character in greeting: # Iterate over the string one letter at a time
	if "-" in character: # if the current character is a hyphen
		print("Hyphen detected, ending loop!")
		break # End the loop
	else:
		print(character) # Print the current character
```



### continue



Continue statements are used to jump to the next iteration. So for example let's say you wanted to print the even numbers from 0-10 using a while loop, you could do it like this:



```python
x = 0 # Initialize a variable to use in the condition

while x < 10:
	if ((x % 2) == 0): # If the number is even
		print(x)
		
	else: # If the number is odd
		continue # Go to next iteration
```



### Loop Tricks and Techniques



Here are some additionally useful things you can do with loops, as well as things to avoid.



#### Infinite Loops



When you are making a *while* loop, inevitably you will create a loop that never ends. Some languages stop you from doing this, python is not one of them. If you create a loop that wont stop, you can force the program to stop running by pressing ctrl+c on windows or cmd+c on mac.



#### Loop Nesting



You can execute loops inside of loops, this is useful in many cases. A good real world example is that some people will put lists inside lists, or dictionaries inside dictionaries. Here is an example of going through a list of shopping lists:



```python
shopping_lists = [["Eggs", "Milk", "Ham"], 
                  ["Vinegar", "Mustard", "Ketchup"], 
                  ["Burgers", "Lettuce", "Mayo"]]

for current_list in shopping_lists: # Steps through the list of lists
    for item in current_list: # Steps through each list
        print(item) # Prints the item in the current shopping list
```



This prints:

```python
Eggs
Milk
Ham
Vinegar
Mustard
Ketchup
Burgers
Lettuce
Mayo
```

