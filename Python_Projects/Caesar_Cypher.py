import sys

sys.path.append("../Python_modules")
from cipher_art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

"""
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
#e.g.
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
#print output: "The encoded text is mjqqt"
##HINT: How do you get the index of an item in a list:
#https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
def encrypt(plain_text, shift_amount):
    cypher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = (position + shift_amount) % 26 # to fix the edge case of letters near the end of the alphabet
        new_letter = alphabet[new_position]
        cypher_text += new_letter
    print(f"The encoded text is: {cypher_text}")
#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
#TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
#e.g.
#cipher_text = "mjqqt"
#shift = 5
#plain_text = "hello"
#print output: "The decoded text is hello"
#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
def decrypt(cypher_text, shift_amount):
    original_text = ""
    for letter in cypher_text:
        position = alphabet.index(letter)
        new_position = (26 + (position - shift_amount)) % 26
        new_letter = alphabet[new_position]
        original_text += new_letter
    print(f"The decoded text is: {original_text}")
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cypher_text=text, shift_amount=shift)
"""

"""#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values."""

def caesar(start_text, shift_amount, cipher_direction):
    # initialize return text
    end_text = ""

    # assign direction for the shifting of the text
    if cipher_direction == "decode":
        shift_amount *= -1

    # loop through each character to encode or decode the text
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)

            # use modulus to prevent list out of range error
            new_position = (position + shift_amount) % 26
            end_text += alphabet[new_position]
        else:
            # include spaces, symbols and numbers in the text w/o being modified
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")

# loops the program so the program does not need to be manually started again
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("Type 'yes' if you want to continue or 'no' if you want to stop\n")
    if result == 'no':
        should_continue = False
        print("Goodbye")



"""
#TODO-1: Import and print the logo from art.py when the program starts.
#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26.
#Hint: Think about how you can use the modulus (%).
#TODO-3: What happens if the user enters a number/symbol/space?
#Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
#e.g. start_text = "meet me at 3"
#end_text = "•••• •• •• 3"
#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
"""