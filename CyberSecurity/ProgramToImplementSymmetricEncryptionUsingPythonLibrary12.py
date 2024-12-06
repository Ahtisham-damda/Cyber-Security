#Program No : 12
#python program to implement symmetric encryption using python library

from cryptography.fernet import Fernet
key=Fernet.generate_key()
f=Fernet(key)
token=f.encrypt(b"Welcome to AIMCA Lab")
print(token)
d=f.decrypt(token)
print(d)



# output 1:
# b'gAAAAABljCEuocTYMjp9a9cABO3kppSTfXXKmDGFNkqr0qUptuNfXjiR0hm1LxroDI4V0eBcnRIiAAKwPzCsoeYxfFSDD8XBHE3rQgM4pbQVmAjLk-YUk='
# b'Welcome to AIMCA Lab