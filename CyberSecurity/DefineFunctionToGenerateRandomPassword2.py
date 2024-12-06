#Program No : 2
#write a python program that defines a function to generate random passwords
# of a specified length the function takes an optional parameter length,which is
# set to 8 by default.if no length is specified by the user,the password will
# have 8 characters


import random
import string
def generate_passwod(length=8):
    all_characters=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(all_characters)for i in range(length))
    return password
password_length_str=input("input the desired legth of your password:")
if password_length_str:
    password_legth=int(password_length_str)
else:
    password_legth=8
    
password=generate_passwod(password_legth)
print(f"Generated password is:{password}") 


# output 1:
# input the desired length of your password:8
# Generated password is:dlm,z3NN
# Output 2:
# input the desired length of your password:10
# Generated password is:b}r-="1lM]