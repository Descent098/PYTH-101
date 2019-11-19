"""
    =========== Challenge 1 =============

    Take two inputs from the command line, then
    convert both to an int the first number will
    be the starting number, and the second will be
    the ending number. Create a loop that goes from
    the starting number to the ending number, and only
    prints the even numbers.
"""

"""
    =========== Challenge 2 =============

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

numbers = [[1,4,7], [2,5,8], [3,6,9]]

x = 0
while x < 3:
    print(numbers[0][x])
    print(numbers[1][x])
    print(numbers[2][x])
    x += 1