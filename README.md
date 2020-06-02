# sha256
A very, very simple program to encrypt a message using hash sha256, commonly used in network security.

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
## Dry Run
```
enter string to encrpyt: hello world
>>> b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9
```
