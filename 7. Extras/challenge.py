"""
    =========== Challenge 1 =============

    Below is a game in which you specify
    how many cookies there are at the beginning.
    on each 'turn' a random amount between 1-10
    of cookies are removed. Once there are no cookies
    use an f-string to print if player 1 (an even number
    of turns) or player 2 (an odd number of turns) won. 
"""
import random

cookies = int(input("How many cookies?: "))

turns = 0

while cookies < 0:

    cookies -= random.randint(0,10)
    turns += 1
