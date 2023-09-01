# def name_of_function():
#   '''
#     hello world
#   '''
#   print("Hello")

# name_of_function()

# def say_hello(name='Default'):
#   print(f'Hello {name}')

# say_hello()

# def add_num(num1, num2):
#   return num1 + num2

# result = add_num(10, 20)

# print(result)

# def even_check(num):
#   return num % 2 == 0

# print(even_check(31))
# print(even_check(30))

# def check_even_list(num_list):
#   # return a list of even numbers
#   even_numbers = []
#   for num in num_list:
#     if num % 2 == 0:
#       even_numbers.append(num)
#     else:
#       pass # don't do anything
#   return even_numbers

# print(check_even_list([13, 37, 44, 55, 60]))
# print(check_even_list([13, 37, 45, 55]))

# tuple unpacking

# stock_prices = [('AAPL', 400), ('MSFT', 300), ('NVDA', 200)]

# for item in stock_prices:
#   print(item)

# for ticker, price in stock_prices:
#   print(ticker)
#   print(price)

# work_hours = [("Abby", 100), ("David",500), ("James", 1000)]

# def employee_check(work_hours):

#   current_max = 0
#   employee_of_month = ''

#   for employee, hours in work_hours: # tuple unpacking
#     if hours > current_max:
#       current_max = hours
#       employee_of_month = employee
#     else:
#       pass
#   return (employee_of_month, current_max) # tuple


# print(employee_check(work_hours))
# # can assign the result to a variable

# result = employee_check(work_hours)
# print(result)

# # or tuple unpacking
# name, hours = employee_check(work_hours)
# print(name)
# print(hours)

### three card monty

# example = [1,2,3,4,5,6,7]

# from random import shuffle

# # shuffle(example)
# # print(example)

# def shuffle_list(mylist):
#   shuffle(mylist)
#   return mylist

# result = shuffle_list(example)
# print(result)


# mylist = [' ', 'O', ' ']
# print(shuffle_list(mylist))

# def player_guess():

#   guess = ''
#   while guess not in ['0', '1', '2']:
#     guess = input("Pick a number: 0,1, or 2 guess:")

#   return int(guess)

# # myindex = player_guess()

# def check_guess(mylist, guess):
#   if mylist[guess] == 'O':
#     print("Correct")
#   else:
#     print("Wrong guess!")
#     print(mylist)

# #initial list
# mylist = [' ', 'O', ' ']

# #shuffle list
# mixedup_list = shuffle_list(mylist)

# #user guess
# guess = player_guess()

# #check guess
# check_guess(mixedup_list,guess)


# def myfunc(a, b, c = 0, d = 0, e = 0):
#   return sum((a, b, c)) * 0.05
#   # sum method requires a tuple for multiple arguments

# print(myfunc(40, 60, 100))

# # *args treats the parameters coming in as a tuple

# def myfunc(*args): # turns the parameters into a tuple for the sum method
#   return sum(args) * 0.05

# print(myfunc(40, 60, 80))

# with *args the user can pass in as many arguments as they want

# def myfunc(*args):
#   for item in args:
#     print(item)

# myfunc(40, 60, 80)

# **kwargs returns dictionary - keyword arguments

# def myfunc(**kwargs):
#   print(kwargs)
#   if 'fruit' in kwargs:
#     print('My fruit of choice is {}'.format(kwargs['fruit']))
#   else:
#     print("I didn't find any fruit here")

# myfunc(fruit='apple', veggie = 'lettuce')

# def myfunc(string):
#     new_word = ''
#     print(range(len(string)))
#     for i in range(len(string)):
#         if i % 2 == 0:
#             new_word += string[i].upper()
#         elif i % 2 == 1:
#             new_word += string[i].lower()

#     return new_word

# print(myfunc('Anthropomorphism'))

#lambda expressions/ functions are one time use

#map function
# def square(num):
#   return num**2

# my_nums = [1, 2, 3, 4, 5]

# for item in map(square, my_nums):
#   print(item)

# # second way to display the map items

# print(list(map(square, my_nums)))

def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ["Philip", "Joe", "David"]

print(list(map(splicer, names)))

# the map function executes the lambda function, we don't envoke the function in the ()

#filter function
def check_even(num):
    return num % 2 == 0

mynums = [1,2,3,4,5,6]

print(list(filter(check_even, mynums)))

for n in filter(check_even,mynums):
    print(n)

#lambda function is an anonymous function
# used for map and filter functions

print(list(map(lambda nums: nums ** 2, mynums)))















  