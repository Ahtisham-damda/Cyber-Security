#Program No:4
#Write a Python program that reads a file containing a list of passwords, one
# per line. It checks each password to see if it meets certain requirements
# (e.g. at least 8 characters, contains both uppercase and lowercase letters,
# and at least one number and one special character). Passwords that satisfy the
# requirements should be printed by the program.


import re
def check_password(password):
    # Password should have at least 8 characters
    if len(password) < 8:
        return False
    # Password should contain at least one uppercase letter.
    if not re.search(r'[A-Z]', password):
        return False
    # Password should contain at least one lowercase letter.
    if not re.search(r'[a-z]', password):
        return False
    # Password should contain at least one number.
    if not re.search(r'\d', password):
        return False
    # Password should contain at least one special character.
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True
# Open the file containing the passwords.
with open('password.txt', 'r') as f:
    # Read the passwords line by line.
    for line in f:
        password = line.strip()
        # Check if the password meets the requirements.
        if check_password(password):
            print(password) 
            
            
# content od password.txt
# Germany#12
# Password5#(%
# helloWoris1234()
# hello331
# output:
# Germany#12
# Password6#(%
# helloWoris1234(
