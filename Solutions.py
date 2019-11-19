"""Here are all the solutions to the exercises and Challenges"""




"""===================== Module 3 ==========================="""

"""
    =========== Challenge 1 =============

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

# This one is pretty hard, in the video for this lesson I explain it in depth.

numbers = [[1,4,7], [2,5,8], [3,6,9]]

x = 0 # Used to count how many itterations to do
while x < 3: # Loop while x is less than the number of sublists in numbers
    print(numbers[0][x]) # Take the first lists x'th term and print it
    print(numbers[1][x]) # Take the Second lists x'th term and print it
    print(numbers[2][x]) # Take the Third lists x'th term and print it
    x += 1 # Increment loop counter by 1