#Program No : 10
#python program to implement asymmetric encryption using RSA python library

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

keyPair=RSA.generate(3072)

pubKey=keyPair.publickey()
#print(f"Public key:(n={hex(pubKey.n)},e={hex(pubKey.e)})")
pubkeyPEM=pubKey.exportKey()
#print(pubkeyPEM.decode('ascii'))

#print(f"Private key:(n={hex(pubKey.n)},d={hex(keyPair.d)})")
privkeyPEM=keyPair.exportKey()
#print(privkeyPEM.decode('ascii'))

#encryption
msg=b'Welcome to AIMCA'
encryptor=PKCS1_OAEP.new(pubKey)
encrypted=encryptor.encrypt(msg)
print("Encrypted:",binascii.hexlify(encrypted))

#decryption
decryptor=PKCS1_OAEP.new(keyPair)
decrypted=decryptor.decrypt(encrypted)
print("Decrypted:",decrypted.decode('utf-8'))


# output :
# Encrypted:
# b'6ebd44a273e1c04bfed82e16d1a99bdec5966ebd51b02c1fd18a02959d932a88f4e9d4843a
# 9d0d1cdf5e1af6d7a5472384921499ac8db00e45fa052b27529f737f16938d815f2637a7690fb
# 9b6e50361cb1049b0801344b7233c215638368df32d7142a96341350093d721fe5b9d1a360a
# 95017a6175b7407ec0ef15951240e71f298004ae020b44eefe06845b78c7d38669bf8379d018
# e0f122c28cf51e97ad4a7ca3b1b64f39ee1583d726a10248724a634726d0b99d121ac1a3243b
# 0378e768d2743f13150c34d9f4efb76d7c9a3c403ac7613102f3291921732754eabe052814b5
# a49951585f302f621a43de6ef43831bac2e30a90a4e5a03ab9684aa42ba1d71366dc9b4a06a6
# bcdb8ed06a5f402da96cff3c0500f2f1c12b96fcee4e2388eee0053b8135c08a61e5cdf1f5e959
# 3602eb0343cd1106014da188f650fa13a43880e763d9065db3f38c884bf8e8643d4bef7cb884
# f809802fbfeaa766e099d5fa68e23376f9ba958c5cb846e7a9a10500fdeb8a3734d0ef598586af
# 18ea4f'
# Decrypted: Welcome to AIMCA