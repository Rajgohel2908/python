f = open("poem.txt")
poem = f.read()
if("twinkle" in poem):
    print("Its talking about twinkle!")
else:
    print("Its not talking about twinkle!")