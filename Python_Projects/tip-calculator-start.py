#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill_amount_no_tax = float(input("What is the total amount on the bill? "))
tip = int(input("How much tip do you want to give? "))

amount_of_people = int(input("How many people are splitting the bill? "))

bill_with_tax = bill_amount_no_tax * (1 + tip/100)
# print(type(bill_amount_no_tax))
# print(bill_with_tax)

bill_per_person = bill_with_tax / amount_of_people

final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount:.2f}")


