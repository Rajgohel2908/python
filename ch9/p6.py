with open("log.txt", "r") as f:
    para = f.read()

if("python" in para):
    print("Its talking about python")
else:
    print("Its not talking about python")