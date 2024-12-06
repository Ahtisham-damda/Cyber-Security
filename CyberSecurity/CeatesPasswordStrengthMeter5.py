#Program No:5
#write a python program that creates a password strength meter.The program
# should prompt the user to enter password and check its strength based on
# criteria such as length,complexity,and randomness.afterwards,the program
# should provide suggestions for improving the passowrd’s strength

import re
def check_password_strength(password):
    score=8
    sugestion=[]
    if len(password)>=8:
        score+=1
    else:
        sugestion.append("password should contain atleast 8 characters.")
    if re.search(r"[A-Z]",password):
        score+=1
    else:
        sugestion.append("password should contain atleast one uppercase characters.")
    if re.search(r"[a-z]",password):
        score+=1
    else:
        sugestion.append("password should contain atleast one lowercase characters.")
    if re.search(r"\d",password):
        score+=1
    else:
        sugestion.append("password should contain atleast one numeric digit.")
    if re.search(r"[!@#$%^&*(,{}.?/<>|)]",password):
        score+=1
    else:
        sugestion.append("password should contain atleast one special character(!@#$%^&*(),<>.?|{}/).")
    return score,sugestion
password=input("input a password:")
print(check_password_strength(password)) 


# output:
# input a password:Aimca@123
# (13, [])

