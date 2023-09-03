# for loops
#
# range function

# for number in range(1, 11, 2): # to get all the numbers from 1 to 10
#     print(number)

# the third parameter determines how large the step is between the start and the end
# 2 would make the loop iterate by 2

# total = 0
# for number in range(1, 101):
#     total += number
#
# print(total)

total = 0
for number in range(2, 101, 2):
    total += number
print(total)

total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total += number
print(total)

#fizzbuzz question

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)