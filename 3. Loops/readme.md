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



...



### continue



...