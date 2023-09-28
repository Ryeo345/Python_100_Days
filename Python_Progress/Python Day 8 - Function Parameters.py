# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

"""
def greet():
    name = input("Enter your name: ")
    print(f"Hello, {name}.")
    print("Welcome to this review.")
    print("Lets see what I can do for you today.")

greet()
"""

# functions with different input can output a different result depending on the inputs

"""
def greet_with_name(name):

    print(f"Hello, {name}.")
    print("Welcome to this review.")
    print(f"Lets see what I can do for you today, {name}.")

name = "John"

    # parameter = argument
    # parameter is the name of the data being passed in
    # argument is the actually value of the data

greet_with_name(name)
"""

# challenge to create a function with 2 parameters

def greet_with_name_location(name, location):
    print(f"Hello {name}")
    print(f"What is the weather like in {location}?")



greet_with_name_location(name = "Phil", location = "New York")

# Positional arguments are arguments passed directly in the ()
# keyword arguments a=1 , b=2, c=3

"""
#create a function to calculate the minimum number of cans to paint a wall with inputted dimensions

#Write your code below this line 👇

import math
def paint_calc(height, width, cover):
    num_of_cans = math.ceil((height * width) / cover)

    print(f"You'll need {num_of_cans} cans of paint.")





#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
"""

# write a function that checks if the inputted number is a prime number

#Write your code below this line 👇

def prime_checker(number):
    is_Prime = True
    for i in range(2, number): # 1 is a not a prime number, range starts at 2 and up to the number - 1
        if number % i == 0:
            is_Prime = False

    if is_Prime: # this test for boolean value
        print("It's a prime number.")
    else:
        print("It's not a prime number.")



#Write your code above this line 👆

#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)