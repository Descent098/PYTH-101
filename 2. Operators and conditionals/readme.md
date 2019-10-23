# Operators and Conditionals



## Operators

Operators are symbols built into python that allow for special functionality such as addition, subtraction and



#### Arithmetic operators

Arithmetic operators are operators used to do basic arithmetic (hence the name). What this means is that they are the basis for any calculations you need to make in a program. Most of these will be pretty obvious so I will try and make it more interesting by telling you some of the usefulness (weirdness) you wouldn't expect out of them, as well as some use cases.

<img src="../Images/Memes/calculation.jpg" alt="calculation" style="zoom:67%;" />



##### Addition

This should be pretty basic and boring, in fact you have already seen it before, but for the sake of completeness, here is how to do addition in python:

```python
print(5 + 3) # Prints: 8

# You can also use variables

sum_value = 5 + 8

print(sum_value) # Prints 8

# You can also use variables in place of numbers

sum_2 = 6 + sum_value 

print(sum_2) # Prints: 14 
```

Well that was boring, **but**... there are more interesting things you can do with addition. For example, if you have multiple lists you can actually add them together to combine the two (order matters):

```python
my_list = [1,2,3,4] # Initialize my_list

my_list_2 = [5,6,7,8] # Initialize my_list_2

my_list = my_list + my_list_2 # Take the current value of my_list and add my_list_2 to it

print(my_list) # Prints: [1, 2, 3, 4, 5, 6, 7, 8]

```

As you can see in the above example, when the my_list_2 variable is added to the first my_list variable it is tacked on to the end of it (called *concatenation* in computer science).



Here is where things get weird, if you recall in the first challenge (yes you should do those), I mentioned that strings are **like** lists. This means operands also work on strings:

```python
name = "Hello " # Set name variable to an string 'hello '

name = name + "World!" # Take the current name value and add 'world' to it

print(name) # Prints: Hello World!
```

Just a heads up combining these properties together gives some interesting effects that I won't go into detail with, but I will show you. For example if you add a string and a list: 

```python
my_list = [] # Initialize an empty list

name = "John" # Initialize name variable to John

my_list = my_list + name # Adding the current my_list variable to the string name

print(my_list) # Prints: ['j','o','h','n']
```

Now this ^^ is weird, the reason is that strings are actually lists of **individual characters**, and so as we saw before they are *concatenated* together.



##### Subtraction

Just like addition, subtraction is somewhat boring the syntax for it is pretty simple:

```python
print(5 - 3) # Prints: 2

# You can also use variables

value = 5 - 8

print(value) # Prints -3

# You can also use variables in place of numbers

value_2 = value - 6 

print(value_2) # Prints: -9
```



Unlike addition there are no fun tricks with it though, subtracting from a string or list will just give you an error. 



##### Multiplication

Now multiplication is back to getting weird. First lets get the simple syntax down: 

```python
print(5 * 3) # Prints: 15

# You can also use variables

value = 5 * 8 

print(value) # Prints 40

# You can also use variables in place of numbers

value_2 = value * 6

print(sum_2) # Prints: 120
```



Now for the weird part, with lists and strings you can multiply them, and the results are very fun...

```python
my_list = [1,2,3,4] # Initialize my_list

my_list = my_list * 3 # Take my_list and multiply it by 3

print(my_list) # Prints: [1,2,3,4,1,2,3,4,1,2,3,4]
```

As you can see, when you multiply a list (or string) by a number, it *concatenates* the value of the list (or string) the number of times you multiply it by. So in this case since the list is multiplied by 3, the value of the list is present 3 times in a row.



##### Division

...



##### Shortcuts

Many of the operations you are doing are going to involve taking the original value of a variable doing an operation and storing the result back in the variable. For example: 

```python
variable_1 = 5 # Initialize the variable to 5

variable_1 = variable_1 + 5 # Take the current value of the variable and add 5

variable_1 = variable_1 - 5 # Take the current value of the variable and subtract 5

variable_1 = variable_1 / 2 # Take the current value of the variable and floating point divide by 2

variable_1 = variable_1 // 2 # Take the current value of the variable and integer divide by 2
```



For addition, subtraction, multiplication and division there is a shortcut to do the above operations. The general form is ```variable_name <operator>= value```

```python
variable_1 = 5 # Initialize the variable to 5

variable_1 += 5 # Take the current value of the variable and add 5

variable_1 -= 5 # Take the current value of the variable and subtract 5

variable_1 /= 2 # Take the current value of the variable and floating point divide by 2

variable_1 //= 2 # Take the current value of the variable and integer divide by 2
```



##### Modulus

What this actually does is returns the **remainder** to the division of the two terms.



#### Logical operators

...

##### Greater than



##### Greater than or equal to



##### Less than



##### Less than or equal to





#### Bitwise operators

...





## Conditionals



### if, else, and elif statements

#### if

...

#### else

....

#### elif

...



### While and break statements

#### While

...

#### break

...