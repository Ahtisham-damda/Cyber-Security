#Program No : 9
# python program implementation for hacking Caeser Cipher algorithm

message='YOU ARE BEAUTIFUL'
LETTERS='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(LETTERS)):
    translated=''
for symbol in message:
    if symbol in LETTERS:
        num=LETTERS.find(symbol) #get the number of the symbol
        num=num-key
        if num<0:
            num=num+len(LETTERS)
        translated=translated+LETTERS[num]
    else:
        translated=translated+symbol
print('key #%s:%s'%(key,translated))

# output:1
# key #25:ZPV BSF CFBVUJGVM 