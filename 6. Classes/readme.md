# 6. Classes

*Since this is such a long and complicated module I have included a glossary at the bottom to help sort things out*

Classes are a way of bundling data (attributes) and functions (sometimes called methods) into abstractions in python.

For example, let's say you are writing an app to store a bunch of data about animals. For this you can set up a class that has the basic attributes of all animals like species name, endemic regions (where it lives), common name (what people know it as) etc.

The python code for this would look like

```python
class Animal:
  def __init__(self, species_name, regions, common_name):
    """A class to represent a generic animal

    Attributes
    ----------
    species_name(str): The technical species name of the animal
    regions(list[str]): A list of regions the animal is endemic to
    common_name(str): The colloquial name of the animal
    """
    self.species_name = species_name
    self.regions = regions
    self.common_name = common_name
```

So we can break down the example in a moment, first let's start with what you can now do with the above class. Once you have a class, it can act as a template to create *instances*. You can think of this with the analogy that a *class* is a cookie cutter, and an *instance* is a cookie that has been cut from the cutter.

Let's use our *Animal class* (cookie cutter) to create an *instance* of a [*Common Leopard Gecko*](https://en.wikipedia.org/wiki/Common_leopard_gecko)(cookie):

```python
leopard_gecko = Animal("Eublepharis macularius",
    ["Afghanistan","Pakistan","India", "Iran"],
    "Common Leopard Gecko")
```

Now that we have have *instantiated* the leopard gecko instance, we can use a simple syntax (```instance.variable_name```) to access the variables. For example if we wanted to know the common name of a *Common Leopard Gecko* we could use:

```python
leopard_gecko.common_name # Returns 'Common Leopard Gecko'
```

We can also add methods (functions) specific to the class, for example let's write a method that prints info about the animal:

```python
class Animal:
  def __init__(self, species_name, regions, common_name):
    """A class to represent a generic animal

    Attributes
    ----------
    species_name(str): The technical species name of the animal
    regions(list[str]): A list of regions the animal is endemic to
    common_name(str): The colloquial name of the animal
    """
    self.species_name = species_name
    self.regions = regions
    self.common_name = common_name
  def print_info(self):
    """Prints information about animal instance"""
    print(f"\nCommon Name: {self.common_name}\nSpecies: {self.species_name}\nRegions: {self.regions}")
```

Now we can take the leopard gecko example from earlier and use our method using the syntax (instance.method()):

```python
leopard_gecko = Animal("Eublepharis macularius", ["Afghanistan","Pakistan","India", "Iran"],"Common Leopard Gecko")

"""Prints (not returns)
Common Name: Common Leopard Gecko
Species: Eublepharis macularius
Regions: ['Afghanistan','Pakistan','India', 'Iran']
"""
leopard_gecko.print_info()
```


There was a lot going on in the last example so lets break down what happened. First we start by *defining* our class (usually called the *class definition*) with:

```python
class Classname: # Notice for classes the convention is to start them with a capital
  def __init__(self): # This method will be explained later on
    pass
```

Following our *class definition* right away we define a ```__init__``` method. The ```__init__``` method is explained in further detail below. But first let's take a look at that funny *self* that we've been putting in front of our variables.

## self; Instance vs Class attributes

As you can see, for all of the *instance attributes*(variables specific to each instance and not the overall class) we are adding a *self* in front with a dot. This is because when we create an *instance*, all of the variables are *localized* to that *instance*.

So for example if we use the animal class from earlier to create two different animal instances, the variables don't overlap.

```python
leopard_gecko = Animal("Eublepharis macularius",
    ["Afghanistan","Pakistan","India", "Iran"],
    "Common Leopard Gecko")

arctic_fox = Animal("Vulpes lagopus",
    ["The Arctic"],
    "Arctic fox")


leopard_gecko.common_name # Returns 'Common Leopard Gecko'

arctic_fox.common_name # Returns 'Arctic fox'
```

This is the same with *instance methods*; The variables it pulls are specific to the *instance* and not the *class*. For example:

```python
leopard_gecko = Animal("Eublepharis macularius",
    ["Afghanistan","Pakistan","India", "Iran"],
    "Common Leopard Gecko")

arctic_fox = Animal("Vulpes lagopus",
    ["The Arctic"],
    "Arctic fox")

leopard_gecko.print_info()
"""Prints (not returns)
'Common Name: Common Leopard Gecko
Species: Eublepharis macularius
Regions: ["Afghanistan","Pakistan","India", "Iran"]'
"""

arctic_fox.print_info()
"""Prints (not returns)
'Common Name: Arctic fox
Species: Vulpes lagopus
Regions: ["The Arctic"]'
"""
```

*Class attributes* on the other hand are attributes that are common among **all** *instances* of a *class*.

For example, let's say you wanted to keep a counter that goes up by 1 for every time a new animal is added. Since this information, is not specific to an *instance*, but rather to every instance of a given *class* you would want it to be accessible to every instance. The code to do something like this would be:

```python
class Animal:
  counter = 0 # Initialize counter to 0
  # This ^^ is a class variable since it is outside of __init__ and has no self. in front
  def __init__(self, species_name, regions, common_name):
    """A class to represent a generic animal

    Attributes
    ----------
    species_name(str): The technical species name of the animal
    regions(list[str]): A list of regions the animal is endemic to
    common_name(str): The colloquial name of the animal
    """
    self.species_name = species_name
    self.regions = regions
    self.common_name = common_name
    Animal.counter += 1 # Accessing and incrementing the class counter by 1 on each instantiation of an Animal
  
  def print_info(self):
    """Prints information about animal instance"""
    print(f"\nCommon Name: {self.common_name}\nSpecies: {self.species_name}\nRegions: {self.regions}")
```

Now there is a counter variable that can be used to find out how many animals have been instantiated

```python
print(Animal.counter) # Prints 0; since no Animal's have been instantiated
leopard_gecko = Animal("Eublepharis macularius",
    ["Afghanistan","Pakistan","India", "Iran"],
    "Common Leopard Gecko")

print(Animal.counter) # Prints 1; since the Leopard Gecko has been instantiated

arctic_fox = Animal("Vulpes lagopus",
    ["The Arctic"],
    "Arctic fox")

print(Animal.counter) # Prints 2; since the Leopard Gecko, and Arctic fox have been instantiated

# Both below calls print 2; Class variables are also accessible in any instance
print(arctic_fox.counter)
print(leopard_gecko.counter)
```

As you can see because the variable belongs to the *class* and not the *instance*, it is available to both the class as a variable, or any *instances* of the *Animal* class.

## ```__init__``` method

The ```__init__``` method in python acts as a [constructor](https://en.wikipedia.org/wiki/Constructor_(object-oriented_programming)) (sort of) in python. This means that it 'constructs' the instance.

In our analogy of a cookie cutter from earlier, the ```__init__``` method would be the actual cutting of the cookie. The method is run every time you *instantiate* an instance. For example when you run the leopard_gecko example from before:

```python
leopard_gecko = Animal("Eublepharis macularius",
    ["Afghanistan","Pakistan","India", "Iran"],
    "Common Leopard Gecko")
```

The variable is making an *implicit* call to ```__init__```, this would roughly be equivalent to:

```python
leopard_gecko = Animal.__init__("Eublepharis macularius",
    ["Afghanistan","Pakistan","India", "Iran"],
    "Common Leopard Gecko")
```

We can see this more clearly by switching examples a bit. Let's take the following class:

```python
class CookieBaker:
  def __init__(self, number_of_cookies):
    """ Example class that is used to show off the __init__ method.
    The __init__ method calls prints 'Cookie Baked' as many times as there are number_of_cookies.

    Attributes
    ----------
    number_of_cookies(int): How many cookies to bake
    """
    print(f"__init__ method called, creating {number_of_cookies} cookie(s):")
    self.number_of_cookies = number_of_cookies
    for cookie in range(number_of_cookies):
      print("Cookie Baked!")
```

As you can see, you can do some basic logic in the ```__init__``` method, such as for loops. You can also call methods, just make sure to include ```self.``` when calling them since you are inside the instance.

For example:

```python
class CookieBaker:
  def __init__(self, number_of_cookies):
    """ Example class that is used to show off the __init__ method.
    The __init__ method calls the bake_cookie() method as many times as there are number_of_cookies.

    Attributes
    ----------
    number_of_cookies(int): How many cookies to bake
    """
    print(f"__init__ method called, creating {number_of_cookies} cookie(s):")
    self.number_of_cookies = number_of_cookies
    for cookie in range(number_of_cookies):
      self.bake_cookie()

  def bake_cookie(self):
    """Print's 'Cookie Baked!'."""
    print("Cookie Baked!")
```

## Additional info (optional)

### Class attributes: Access

Keep in mind that like other variables python will let you override class variables **without question**. So they can be modified from the *class* at will. For example:

```python
print(Animal.counter) # Prints 0; since no Animal's have been instantiated
leopard_gecko = Animal("Eublepharis macularius",
    ["Afghanistan","Pakistan","India", "Iran"],
    "Common Leopard Gecko")

print(Animal.counter) # Prints 1; since the Leopard Gecko has been instantiated

Animal.counter = 35 # Overriding the variable from the class

print(Animal.counter) # Prints 35; since the attribute has been overridden
print(leopard_gecko.counter) # Prints 35; since the attribute has been overridden
```

**But** if you try to modify a class variable from an instance, then it will create an *instance* variable that is now local to the instance while leaving the class variable in tact:

```python
print(Animal.counter) # Prints 0; since no Animal's have been instantiated
leopard_gecko = Animal("Eublepharis macularius",
    ["Afghanistan","Pakistan","India", "Iran"],
    "Common Leopard Gecko")

print(Animal.counter) # Prints 1; since the Leopard Gecko has been instantiated

Animal.counter = 35 # Overriding the variable from the class

print(Animal.counter) # Prints 35; since the attribute has been overridden

leopard_gecko.counter = 26 # creating an instance variable from the class attribute

print(Animal.counter) # Prints 35; since the class attribute WONT be modified by changing the gecko instance counter
print(leopard_gecko.counter) # Prints 26; since the instance attribute has been created
```

### Dataclasses in python

If you are just storing variables there is also a useful module inside the python standard library called [dataclasses](https://docs.python.org/3/library/dataclasses.html) this library makes creating useful classes that just store data much faster.

Let's take a look at this example:

```python
import datetime
class user:
  def __init__(self, name, age, sign_up_date, birthday, premium_member):
    """A class to represent a generic animal

    Attributes
    ----------
    name(str): The technical species name of the animal
    age(str): A list of regions the animal is endemic to
    sign_up_date(datetime.datetime): A datetime object of the day the user signed up
    birthday(datetime.datetime): A datetime object of the users birthday
    premium_member(bool): Whether the user is on premium or free subscription
    """
    self.name = name
    self.age = age
    self.sign_up_date = sign_up_date
    self.birthday = birthday
    self.premium_member = premium_member
```

Now thats a lot of *self.attribute_name*'s, dataclasses will automate the ```__init__``` method (and [```__repr__```](https://docs.python.org/3/reference/datamodel.html#object.__repr__) method).

The same class can be written like this:

```python
import datetime
from dataclasses import dataclass

@dataclass
class user:
    """A class to represent a generic animal

    Attributes
    ----------
    name(str): The technical species name of the animal
    age(str): A list of regions the animal is endemic to
    sign_up_date(datetime.datetime): A datetime object of the day the user signed up
    birthday(datetime.datetime): A datetime object of the users birthday
    premium_member(bool): Whether the user is on premium or free subscription
    """
    name:str
    age:str
    sign_up_date:datetime.datetime
    birthday:datetime.datetime
    premium_member:bool
```

For more details check out: https://github.com/canadian-coding/posts/tree/master/2019/August/19th%20-%20Dataclasses%20in%20Python

## Glossary

*Class*: A template to create *Instance(s)/Object(s)* from. Classes exist to bundle data (attributes) and functions (methods) into abstractions that are meaningful. A good analogy is to think of a cookie cutter as a class, that is a template used to cut (*instantiate*) cookies (*Instance(s)/Object(s)*)

For example you could have an Animal class that can be used to create *Instance(s)/Object(s)* to bundle data and functions about animals, or a user class that can be used to create *Instance(s)/Object(s)* to bundle data and functions about each user of an app.

*Instance/Object*: An object representing something, created from a class (used as a template). A good analogy is to think of a cookie cutter as a class, that is a template used to cut (*instantiate*) cookies (*Instance(s)/Object(s)*).

For example if you had an Animal class, you could use it to *instantiate* a leopard gecko instance that has all the data (attributes) and functions (methods) necessary to represent a leopard gecko.

In python people use *Instance* and *Object* interchangeably, and the same is true for many other object-oriented languages.

*Instantiate*: The act of creating (initializing) an *Instance/Object* from a *class*. A good analogy is to think of a cookie cutter as a *class*, that is a template used to cut (*instantiate*) cookies (*Instance(s)/Object(s)*)

*Attribute*: A variable that is specific to a *class* or *Instance/Object*.

*Method*: A function that is specific to a *class* or *Instance/Object*.

*Constructor*: What typically gets called on *instantiation* of an *Instance/Object*. This is a concept used broadly in object-oriented languages, but in python this roughly corresponds to the ```__init__``` method.
