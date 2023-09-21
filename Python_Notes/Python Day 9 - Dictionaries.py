"""
Dictionaries have two parts
1. the key is equivalent to the word in a real dictionary
2. the value is equivalent to the definition in a real dictionary

dictionary values are identified by their keys, instead of indexes in a list

dictionary[key] = value

adding new elements to the dictionary
dictionary[new_key] = new_value

create empty dictionary = {}

wipe existing dictionary = {}

example of use, restart a game and clear all stats of the user

edit value of dictionary
dictionary[key] = new_value_2

loop through a dictionary

for thing in dictionary:
    print(thing)

this will print all the keys, not the values

for key in dictionary:
    print(key)
"""

# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }

# for item in programming_dictionary.items():
#     # print(key) #key
#     # print(programming_dictionary[key]) #value
#     # print(key)
#     # print(value)
#     # items() method unpacks the dictionary
#     print(item) # turns the dictionary into a tuple of key and values


# exercise to create a new dictionary from an old dictionary

# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# # 🚨 Don't change the code above 👆
#
# #TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}
#
# #TODO-2: Write your code below to add the grades to student_grades.👇
# for student, score in student_scores.items():
#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif 80 < score < 91:
#         student_grades[student] = "Exceeds Expectations"
#     elif 70 < score < 81:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"
#
#
# # 🚨 Don't change the code below 👇
# print(student_grades)

"""Nesting dictionaries can have lists, and more dictionaries as values"""

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    }
}

# can have multiple dictionaries in a list
