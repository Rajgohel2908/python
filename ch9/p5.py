words = ["donkey", "farmer", "people"]

para = ""
with open("para2.txt","r") as f:
    para = f.read()

for i in words:
    para = para.replace(i , "#" * len(i))

with open("para2.txt","w") as f:
    f.write(para)