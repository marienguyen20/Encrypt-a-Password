import base64
password = "my_password".encode("utf-8")

encoded = base64.b64encode(password)
print(encoded)

# OUTPUT
b'bXlfcGFzc3dvcmQ='

decoded = base64.b64decode(encoded)
print(decoded)

# OUTPUT
b'my_password'
