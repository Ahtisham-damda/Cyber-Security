#Program No:6
#write a python program that reads a file containing a list of usernames and
# passwords.One pair per line(seperatized by a comma).it checks each password to
# see if it has been leaked in a databreach.you can use the "Have I Been Pwned
# "API (https://haveibeenpwned.com)/API/v3) to check if a password has been
# leaked

import requests
import hashlib

with open('passwords.txt','r') as f:
    for line in f:
        username,password=line.strip().split(',')
        password_hash=hashlib.sha1(password.encode('utf8')).hexdigest().upper()
        
response=requests.get(f"https://api.pwnedpasswords.com/range/{password_hash[:5]}")

if response.status_code==200:
        hashes=[line.split(':')for line in response.text.splitlines()]
        for h,count in hashes:
                if password_hash[5:]==h:
                    print(f"password for user {username} has been leaked
{count} times.")
                    break
                else:
                        print(f"could not check password for user {username}.")
                        
                        
                        
# contents of passwords.txt
# user1,Pas1$Kul
# user2,password
# user3,password123
# user4,password123$
# user5,password6#(%
# user6,Germany#12
# output:
# password for user 1 has been leaked 251686 times
# password for user 2 has been leaked 9659369 times
# password for user 3 has been leaked 251656 times
# password for user 4 has been leaked 514 times
# password for user 5 has been leaked 846211 times
# password for user 6 has been leaked 1 times

