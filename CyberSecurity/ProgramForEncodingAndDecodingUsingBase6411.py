#Program No : 11
#python program for encoding and decoding using Base64

import base64
def base64_encode(text):
    encoded_bytes=base64.b64encode(text.encode('utf-8'))
    encoded_text=encoded_bytes.decode('utf-8')
    return encoded_text

#function to decode a base64 string
def base64_decode(encoded_text):
    decoded_bytes=base64.b64decode(encoded_text.encode('utf-8'))
    decoded_text=decoded_bytes.decode('utf-8')
    return decoded_text

#sample text to encode
text_to_encode="Hello,Base64 Encoding and decoding!"

#encode the text to Base64
encoded_text=base64_encode(text_to_encode)

#print the encoded text
print("Encoded Text: "+encoded_text)

#Decode the encoded text
decoded_text=base64_decode(encoded_text)

# print the decoded text
print("decode Text: "+decoded_text)


# output 1:
# Encoded Text: SGVsbG8sQmFzZTY0IEVuY29kaW5nIGFuZCBkZWNvZGluZyE=
# decode Text: Hello,Base64 Encoding and decoding!