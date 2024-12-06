#Program No : 7
#write a python program that simulates a Brute-force attack on a password by
# trying out all possible character combination

import itertools
import string
def bf_attack(password):
    char=string.printable.strip()
    attempts=0
    for length in range(1,len(password)+1):
        for guess in itertools.product(char,repeat=length):
            attempts+=1
            guess=".join(guess)"
            if guess==password:
                return(attempts,guess)
    return(attempts,None)
password=input("Enter password:")
attempts,guess=bf_attack(password)
if guess:
    print(f"Password cracked in {attempts} attempts. the password is{guess}")
else:
    print(f"Password not carcked after {attempts} attempts") 
    
    
    # output:
# Enter password:2424
# Password not carcked after 78914410 attempts
