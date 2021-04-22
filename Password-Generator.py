# ..................................................5 Password Generator....................................
import random

R_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
R_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
R_symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("\n\n\t\t\tWelcome to the PyPassword Generator!\n")
alphabets = int(input("How many letters would you like in your password?\n"))
numbers = int(input(f"How many numbers would you like?\n"))
symbols = int(input(f"How many symbols would you like?\n"))


# # Easy Level
# password = ""
# for alpha in range(1, alphabets+1):
#     letters = random.choice(R_alphabets)
#     password += letters
#     # print(password)
#
# #     OR
# # for alpha in range(1, alphabets+1):
# #     password += random.choice(R_alphabets)
#
# for alpha in range(1, numbers+1):
#     num = random.choice(R_numbers)
#     password += num
#     # print(password)
#
# for alpha in range(1, symbols+1):
#     sym = random.choice(R_symbols)
#     password += sym
#     # print(password)
# print(password)
# # random_pass = random.

# Hard Level


password = []
for alpha in range(1, alphabets+1):
    letters = random.choice(R_alphabets)
    password += letters
    # print(password)

#     OR
# for alpha in range(1, alphabets+1):
#     password += random.choice(R_alphabets) If this didn't work use append()

for alpha in range(1, numbers+1):
    num = random.choice(R_numbers)
    password += num
    # print(password)

for alpha in range(1, symbols+1):
    sym = random.choice(R_symbols)
    password += sym
    # print(password)
# print(f"Password: {password}")
random_pass = random.shuffle(password)
# print(f"Random Password: {password}")

# To make it in string

myPass = ""
for passwd in password:
    myPass += passwd

print(f"Your Password is: {myPass}")



