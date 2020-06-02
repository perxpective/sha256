# sha256
Encrypt a message using hash sha256.

I import the `hashlib` library so that I am able to perform sha256 functions.
```python
import hashlib
```

I prompt the user for a string input. After which, the string input gets encoded using functions below, storing the encoded values into a new variable `encode`.

```python
text = input('enter string to encrpyt: ')
encode = hashlib.sha256(text.encode())
```

Output the result.
```python
print(encode.hexdigest()) 
```
