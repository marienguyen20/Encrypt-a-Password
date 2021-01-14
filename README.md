# Encrypt a Password in Python 

Encrypting a password encodes the password into a randomized sequence of characters.

Use base64.b64encode() to encrypt a password.

Call str.encode("utf-8") to encode a password str into a UTF-8 string. 
Call base64.b64encode(utf_string) to encode the utf_string from the previous step into a base 64 string. 
Call base64.b64decode(b64_string) to decode the b64_string back into a str.
