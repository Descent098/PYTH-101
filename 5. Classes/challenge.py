"""This challenge is very open ended, i'm leaving a lot of the details up to you. Because of this, the challenge is quite difficult if you have never dealt with classes in any languages before.



 ======================== Challenge ========================

Read into inheritance in python: https://www.w3schools.com/python/python_inheritance.asp

Now write a Product class that extends Item, that includes:
    1. nutritional information (A dictionary with values from here: https://schema.org/NutritionInformation such as calories, carbohydrateContent etc.).
    2. A method that prints the nutrition info of a Product into a easily readable format
    3. An expiry attribute that is a datetime.date object: https://docs.python.org/3/library/datetime.html
    4. A method that checks the current date, and returns True if the product has expired, and False if it has not yet expired
"""

class Item:
    def __init__(self, category):
        """ A class representing an inventory item for a company.
        Attributes
        ----------
        category(str): A representation of the general category of an item

        id(str): A unique ID for the item (note this is generated in __init__ and not a parameter passed on instantiation)
        """
        import uuid # Generates a unique ID
        self.id = uuid.uuid4() # Assigns a unique ID to an object
        self.category = category