import string # Helps to define alphabets and punctuation marks
import secrets

letters = string.ascii_letters # Provides both lowercase and uppercase letters
digits = string.digits # PRovides digits 0-9
special_chars = string.punctuation # Provides punctutation marks {special characters}

# Creates a library of alphabets including letters numbers and special characters
alphabet = letters + digits + special_chars

# Password length
pwd_length = int(input('Password length: '))
while True:
    pwd = ""

    # Secret.choice(alphabet) returns a single character from the alphabet library at random
    # the join method adds the generated character to the pwd string...the "" eliminates white space
    # The loop goes through the joining 12 times to create 12 different characters
    for i in range(pwd_length):
        pwd += "".join(secrets.choice(alphabet))
    
    if (any(char in special_chars for char in pwd) and sum(char in digits for char in pwd)>=2):
        break

print(pwd)
