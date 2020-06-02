import hashlib
text = input('enter string to encrpyt: ')
encode = hashlib.sha256(text.encode())
print(encode.hexdigest()) 
