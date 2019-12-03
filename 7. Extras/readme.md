# Extras



This module contains some extra bits and pieces that are useful but didn't fit anywhere else in the course.



## Format Strings

Format strings are a way to add variables into strings in python. They are incredibly useful in all sorts of applications, like greeting a user with their name when they login to an app, or writing a preformatted message to tell people the temperature etc. Basically anywhere that you would normally want to print a variable, format strings are usually the best option. They come in a few formats, but I'm only going to show you the 'recommended one' (see end of this section for details about others). 



To use format strings simply add an f before your quotes (double or single) to declare a string, and where you want a variable to appear add it in between curly braces. For example let's say you wanted to greet someone when they login, the code could look like this:

```python
name = "John Doe"

greeting = f"Welcome, {name}!"

print(greeting) # Prints: Welcome John Doe!
```

One thing to remember with these strings is that they are **created on call**, meaning they only update when they are created and not when the variable is updated. For example:

```python
name = "John Doe"

greeting = f"Welcome, {name}!"

name = "Kieran Wood"

print(greeting) # Prints: Welcome John Doe!

greeting = f"Welcome, {name}!" # Since it's recreated it picks up the new value of name

print(greeting) # Prints: Welcome Kieran Wood!
```



I wrote a post with more information about this [here]( https://canadiancoding.ca/posts/details/8/ )



## Dates

python comes with a great module for handling dates and times called datetime. Here are some examples of basic usage of the module:



### Create Date object

The module works off of classes that you can use to create objects, to create a simple date object you just need to provide 3 attributes, a year (int), a month (int), and day (int):

```python
import datetime

appolo_11_launch = datetime.date(1959, 9, 13)
```



### Compare date objects

You can make comparisons to date objects the same way you would regular numbers:

```python
import datetime

appolo_11_launch = datetime.date(1959, 9, 13)

falcon_9_first_launch = datetime.date(2010, 6, 4)

print(falcon_9_first_launch > appolo_11_launch) # prints: True
```



### Get date object attributes

You can get the attributes of a date object (the year, month, day) the same way you access class attributes:

```python
import datetime

appolo_11_launch = datetime.date(1959, 9, 13)

appolo_11_launch.year # prints: 1959

appolo_11_launch.month # Prints: 9

appolo_11_launch.day # Prints: 13
```



### Get Current Date

You can get the current date using the datetime.date.today() function, which returns a datetime object of today's date:

```python
import datetime

current_datetime = datetime.date.today() # Returns datetime object of todays date
```



## Files



Opening, reading and writing files is an essential part of many apps. I will show you the short (and recommended) way to do this in python.



Every file in python needs to go through 3 steps:

1. Being opened
2. Read from or written to
3. Being 'closed'



Normally each step would have to be done explicitly, but python comes with a handy *with* operator that makes this simple:

```python
with open("filename.extension", "r") as short_name:
```



So what does all this mean, open() is the function you use to open a file, it takes two arguments the filename (with the extension, i.e. '.txt') as a string, and the 'mode' (read, write etc. See [here]( https://docs.python.org/3/library/functions.html#open ) for the documentation about the different modes) and then *as short_name* where short_name is just a arbitrary variable name used to reference the open file.



Using this you can write something similar to a loop to do what you need to do. Let's say for example you wanted to write a bunch of text (in this case *Do not go gentle into that good night -Dylan Thomas 1914-1953*) to a file called 'poem.txt', here is what the code would look like:

```python
text = """Do not go gentle into that good night,
Old age should burn and rave at close of day;
Rage, rage against the dying of the light.

Though wise men at their end know dark is right,
Because their words had forked no lightning they
Do not go gentle into that good night.

Good men, the last wave by, crying how bright
Their frail deeds might have danced in a green bay,
Rage, rage against the dying of the light.

Wild men who caught and sang the sun in flight,
And learn, too late, they grieved it on its way,
Do not go gentle into that good night.

Grave men, near death, who see with blinding sight
Blind eyes could blaze like meteors and be gay,
Rage, rage against the dying of the light.

And you, my father, there on the sad height,
Curse, bless, me now with your fierce tears, I pray.
Do not go gentle into that good night.
Rage, rage against the dying of the light."""

with open("poem.txt", "w+") as poem_file:
    poem_file.write(text)
```



For more details on the different functions available with a file, check out the official python documentation [here]( https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects )



### JSON Files

Another common format (so common it is built in) for files is .json files. In python there is a dedicated json module built into the language to help serialize (write data to a json file), and deserialize (read from a json file) json files.



json files can be opened like normal files, but they have a special way of storing and reading data. There are two functions built into the json module that help with this dump() and load(). dump() takes two arguments, the data you want to store, and the **open** file to write it to. The dump() function let's you store lists, dictionaries, strings, booleans etc. Here is an example of it working:

```python
user = {
	"Name": "Kieran",
	"Age": 21,
	"Canadian": True
}
with open("test.json", "w+") as json_file:
	json.dump(user, json_file)
```



Now to load that data back we can use load() which just takes the **open** file as an argument:

```python
with open("test.json", "r") as json_file:
	user = json.load(json_file)

print(user) # Prints: {'Name': 'Kieran', 'Age': 21, 'Canadian': True}
```



## OS Calls

Usually if you need to get some information about the system a user is on there are two modules that have what you need, [sys]( https://docs.python.org/3.8/library/sys.html ) and [os]( https://docs.python.org/3.8/library/os.html ). Both are built in to python and let you access operating system, and general system information.



For example if you need to find out what os a user is on (mac, windows, or linux) you can use the os module:

```python
import os

if os.name == "nt":
	print("You are on Windows!")

else:
	print("You are on Mac/Linux!")
```



Or let's say you want to force close python for some reason you can with sys.exit():

```python
import sys

sys.exit()
```





