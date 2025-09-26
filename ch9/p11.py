import os

with open("para.txt") as f:
    content = f.read()

os.remove("para.txt")

with open("para_copy.txt", "w") as f:
    f.write(content)