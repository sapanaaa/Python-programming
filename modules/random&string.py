#a password generator using string and random modules
import string
import random

def generatePassword(size):
    all_characters= string.ascii_letters+ string.digits
    password=""
    for character in range(size):
        randomChar= random.choice(all_characters)
        password=password+randomChar
    return password
Size=int(input("How many characters do you want?"))
if (Size<8):
      print("Password is too short!! Cannot generate")
else:
    newPassword=generatePassword(Size)
print("Here is your generated password:", newPassword)    