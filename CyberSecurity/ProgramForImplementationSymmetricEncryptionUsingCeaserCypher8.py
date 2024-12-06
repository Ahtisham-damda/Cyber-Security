#Program No : 8
#python program for implementation symmetric encryption using Ceaser cypher
#algorithm

def caesae_cipher(text,shift):
    encrypted_text=""
    for char in text:
        if char.isalpha():
            shifted_char=chr(ord(char)+shift)
            encrypted_text+=shifted_char
        else:
            encrypted_text+=char
        return encrypted_text
plaintext=input("Enter the text to encrypt:")
shift=3
encrypted_text=caesae_cipher(plaintext,shift)
print("Encrpyted Text is:",encrypted_text) 


# output:
# Enter the text to encrypt:hello AImca
# Encrpyted Text is: khoor DLpfd

