rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

options = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice >= 3:
    print("You typed and invalid number. You lose!")
else:
    print(options[choice])

    computer_choice = random.randint(0, len(options) - 1)

    print(f"Computer chose: \n {options[computer_choice]}")
    if choice == computer_choice:
        print("It is a draw")
    elif choice == 0 and computer_choice == 2:
        print('You Win!')
    elif computer_choice == 0 and choice == 2:
        print('You Lose!')
    elif choice > computer_choice:
        print('You Win!')
    elif choice < computer_choice:
        print('You Lose!')


# can't use options[choice] in the if and elif statements because there is a indexError: out of range if the input is higher than 2

# the rest of the code after the first print statement needs to be tabbed over to continue only if the user choice is in range