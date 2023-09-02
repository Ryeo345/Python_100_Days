# import random
#
# random_integer = random.randint(1, 10)
# print(random_integer) # randomly generates an integer number between 1 and 10
#
# random_float = random.random()
# print(random_float) # random number between 0.0 and 1.0 but not including them
#
# print(random_float * 5)
#
# # how do you create a random decimal number between 0 and 5
# #solution 1
# random_float = random.uniform(0.0, 5.0) # uniform method allows us to change the range of the randomisation
#
# print(random_float)
#
# #solution 2 - multiple random.random() by 5
#
# love_score = random.randint(1, 100)
# print(f"Your Love score is  {love_score}")

# Lists
"""
Lists use square brackets and store objects

we use append method to add to the end of the list

we use extend method to add a list of objects to the end of the list
"""

# randomise who has to pay the bill
# Import the random module here

# Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
#
# import random
#
# random_idx = random.randint(0, len(names) - 1)
#
# random_name = names[random_idx]
#
# print(f"{random_name} is going to buy the meal today!")

# person_who_will_pay = random.choice(names) # choice method randomise one of the names in the list