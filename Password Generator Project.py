# Importing the random module to generate random characters 
import random

# Lists of characters to be used in generating the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x,' 'y', 'z', 'A', 'B', 'C' 'D' 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4','5', '6', '7', '8','9']
symbols = ['!', '#', '$', '%', '&', '*', '(', ')', '+', '@']

# Welcome message and prompting user for password criteria
print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))

nr_symbols = int(input("How many symbols would you like?\n"))
 
nr_numbers = int(input("How many numbers would you like?\n"))

# List to store generated password
password_list = []

# Generating random letters for the password
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

# Generating random symbols for the password
for char in range(1, nr_symbols + 1): 
    password_list += random. choice(symbols)

# Generating random numbers for the password
for char in range (1, nr_numbers + 1):
    password_list += random.choice(numbers)

# Shuffling the password characters to enhance security
random.shuffle(password_list)

# Converting the password list to a string
password = ""
for char in password_list:
    password += char

# Displaying the generated password
print(f"Your password is : {password}")    
