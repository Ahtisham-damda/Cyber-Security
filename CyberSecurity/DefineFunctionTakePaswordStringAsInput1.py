# Program Number:1
# write a program that defines a function and takes a password string as input


import hashlib
def hash_password(password):
    password_bytes=password.encode('utf-8')
    hash_obj=hashlib.sha256(password_bytes)
    password_hash=hash_obj.hexdigest()
    return password_hash

password=input("Enter password:")
hashed_password=hash_password(password)
print(f"Hashed password:{hash_password(password)}")



# output 1:
# Enter password:aimca@123
# Hashed
# password:80dc35998cb52f268d24d4b96bae3fad45a85fb94bb01517a4853b092572b205
# Output 2:
# Enter password:Labadmin@987
# Hashed password:208b7fe9afd8df9307549edfa36172832a906adf9f40bb99c23efaa3a59a04bc