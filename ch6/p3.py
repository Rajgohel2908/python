a = "make a lot of money"
b = "buy it now"
c = "subscribe now"
d = "click this"

com = input("Enter text:")

if((a in com) or (b in com) or (c in com) or (d in com)):
    print("its a spam")
else:
    print("Not a spam")