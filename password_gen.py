import string # Helps to define alphabets and punctuation marks
import secrets
import json
import re
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
    
    # Checks if the password (pwd) has at least one special character and at least two digits
    if (any(char in special_chars for char in pwd) and sum(char in digits for char in pwd)>=2 and not re.search(r'[\/"@\']', pwd)):
        save = input('Do you want to save(y/n): ').capitalize()
        if save == 'Y':
            purpose = input('Password is for: ')
            print('Password Saved!!!')
            pass_dict = {purpose: pwd}
            json_dict = json.dumps(pass_dict)
            # Open (Creates the file if it doesn't exist) the password file and append write the password and the purpose
            with open('Passwords.txt', 'a') as file:
                file.write(json_dict + '\n')
                break
        else:
            break

print(pwd)
