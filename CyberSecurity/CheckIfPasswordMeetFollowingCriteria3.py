#Program No: 3
# write a python program to check if a passwords meets the following criteria:
# a. At least 8 character long,
# b. Contains at least one uppercase letter, one lowercase letter ,one digit and
# on especial character(!,@,#,$,% or &)
# c. if the password meets the criteria, print a message that say’s ”Valid
# Password” . if doesn’t than print the message that say’s ”Password does not
# meet the requirements.”

import re
def validate_password(password):
    if len(password)<8:
        return False
    if not re.search(r'[A-Z]',password):
        return False
    if not re.search(r'[a-z]',password):
        return False
    if not re.search(r'\d',password):
        return False
    if not re.search(r'[!@#$%^&*(),.?:{}|<>]',password):
        return False
    return True
password=input("Input your password:")
is_valid=validate_password(password)
if is_valid:
    print("Valid password.")
else:
    print("not Valid.") 
    
    
#     output 1:
# Input your password:Aimca@123
# Valid password.
# Output 2:
# Input your password:imdgwq
# not Valid.