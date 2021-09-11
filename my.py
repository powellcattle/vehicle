import base64

with open("images/c10.JPG", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())

print(type(str))