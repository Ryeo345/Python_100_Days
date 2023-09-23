"""
Exercise 1 create a function to capitalize the first and last names
returns a value
"""
# def format_name(f_name, l_name):
#     full_name = ""
#     # formatted_f_name = f_name[0].upper() + f_name[1:].lower()
#     # formatted_l_name = l_name[0].upper() + l_name[1:].lower()
#     # full_name = formatted_f_name + " " + formatted_l_name
#
#     if f_name == "" or l_name == "":
#         # return      # returns None if the parameters have no arguments
#         return "You did not provide valid inputs." # error handling
#     full_name = f"{f_name} {l_name}"
#     formatted_full_name = full_name.title()
#     return formatted_full_name # returns the output that we can store in a variable
#
# new_format = format_name(input("What is your first name?\n"), input("What is your last name?\n"))
# print(new_format)
#
# # an empty return ends the function quicker and returns None

"""Exercise 2 check the amount of days in month"""

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
# def days_in_month(year, month):
#     # edge cases
#     # if month > 12 or month < 1:
#     #     return "Invalid month"
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     check_leap_year = is_leap(year)
#     if check_leap_year and month == 2:
#         return 29
#     return month_days[month - 1]
#
# #🚨 Do NOT change any of the code below
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

